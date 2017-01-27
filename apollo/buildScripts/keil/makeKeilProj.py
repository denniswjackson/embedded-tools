# This script constructs a keil project file and a corresponding plain make file.
# The former can be used in development for building and debugging. The latter
# can be used for deployment and release. The advantage to the Makefile is that
# it can be built very quickly on servers which may not have (and definitely
# don't need) the full Keil IDE.
#
# This script does not construct the keil project options file, which does not contain
# build settings. The options file will be generated using defaults the first time the
# project is opened in the IDE
#
# This script was developed for Keil uVision V5.10.0.2
__author__ = 'jstevenson'

import argparse
import os
import shutil
import xml.etree.ElementTree as ET
from cStringIO import StringIO

# Get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--template', required='true', help="The location and name of project file template")
parser.add_argument('--output', required='true', help="The location and name of the output project file")
parser.add_argument('--target', required='true', help="The location and name of the output hex file")
parser.add_argument('--build', required='true', help="The location of the build folder")
parser.add_argument('-I', help="Include paths, absolute or relative to current working directory")
parser.add_argument('-D', help="All preprocessor directives, separated by whitespace, no \';\' required" )
parser.add_argument('--scatter', required='true', help="Scatter file path" )
parser.add_argument('--asm', default="", help="All assembler directives, separated by whitespace, no \';\' required" )
parser.add_argument('--group', action='append', help="A group of source files or libraries in format \"groupName file1 file2, ... fileN\" paths are relative to current working directory" )
args = parser.parse_args()

## Load XML tree from template
projTree = ET.parse( args.template )
projRoot = projTree.getroot()

# Create the makefile stream
genMake = StringIO()

# Extract paths and filenames from args
targetName = os.path.splitext( os.path.basename(args.target) )[0]
targetPath = os.path.dirname( args.target )
projectDir = os.path.dirname( args.output )

# Set target name
projRoot.find('./Targets/Target/TargetName').text = targetName

# Set build directory (which Keil calls the output directory, since the .hex and .o are all put in the same place)
relativeOutputDir = os.path.relpath( args.build, projectDir )
projRoot.find('./Targets/Target/TargetOption/TargetCommonOption/OutputDirectory').text = relativeOutputDir + '\\'

# Set name of output hex, and output directory for .map file (listing path)
projRoot.find('./Targets/Target/TargetOption/TargetCommonOption/OutputName').text = targetName
relativeListingPath = os.path.relpath( targetPath, projectDir )
projRoot.find('./Targets/Target/TargetOption/TargetCommonOption/ListingPath').text = relativeListingPath + '\\'

# Set the scatter file in the project
projRoot.find('./Targets/Target/TargetOption/TargetArmAds/LDads/ScatterFile').text = os.path.relpath( args.scatter, projectDir )

# Set include paths
includePaths = ""
makeIncludes = ""
if args.I:
    for incPath in args.I.split():
        absIncPath = os.path.abspath( incPath )
        try:
            # not all include paths will have a clean relative mapping
            # attempt to convert to relative and if it fails just use
            # absolute. This can happen for example on teamcity where
            # the source is cloned in D:\ but we're including files
            # from the Keil base installation on C:\
            relativeIncPath = os.path.relpath( absIncPath, projectDir )
        except ValueError:
            relativeIncPath = absIncPath

        includePaths = includePaths + relativeIncPath + ";"
        makeIncludes = makeIncludes + "-I \"{0}\" ".format( absIncPath )
    includePaths = includePaths[:-1] # Get rid of trailing ';'
    projRoot.find('./Targets/Target/TargetOption/TargetArmAds/Cads/VariousControls/IncludePath').text = includePaths

# Set preprocessor definitions
makeDefines = ""
if args.D and args.D.strip() != "":
    projRoot.find('./Targets/Target/TargetOption/TargetArmAds/Cads/VariousControls/Define').text = args.D
    makeDefines = "-D" + " -D".join( args.D.strip().split() )

# Set assembler flags
if args.asm and args.asm.strip != "":
    projRoot.find('./Targets/Target/TargetOption/TargetArmAds/Aads/VariousControls/MiscControls').text = args.asm

# All this should really be done with make pattern rules, which would simplify this immensely.
cppDependRuleStr = "$(ARM_CXX) {0} --omf_browse $(basename $@).crf --depend=$(basename $@).d --no_depend_system_headers $(ARM_CXXFLAGS) {1}\n".format( makeIncludes, makeDefines )
cDependRuleStr = "$(ARM_CC) {0} --omf_browse $(basename $@).crf --depend=$(basename $@).d --no_depend_system_headers $(ARM_CFLAGS) {1}\n".format( makeIncludes, makeDefines )
cppRuleStr = "$(ARM_CXX) {0} --omf_browse $(basename $@).crf -o $@ -c $< $(ARM_CXXFLAGS) {1}\n".format( makeIncludes, makeDefines )
cRuleStr = "$(ARM_CC) {0} --omf_browse $(basename $@).crf -o $@ -c $< $(ARM_CFLAGS) {1}\n".format( makeIncludes, makeDefines )
asmRuleStr = "$(ARM_AS) {0} $(ARM_ASFLAGS) {1} -o $@ $<\n".format( makeIncludes, args.asm )

# Add all files to project
linkObjList = []
if args.group:

    # Add each group
    targetsEl = projRoot.find('./Targets/Target')
    groupsEl = ET.SubElement(targetsEl, 'Groups')

    for group in args.group:

        # Add group
        groupNameStr = group.split()[0]
        groupFilesStr = group.split()[1:]
        groupEl = ET.SubElement( groupsEl, "Group" )
        groupNameEl = ET.SubElement( groupEl, "GroupName" )
        groupNameEl.text = groupNameStr

        # Add source and library files in the group to the project and the filter
        filesEl = ET.SubElement( groupEl, "Files" )
        for filename in groupFilesStr:
            fileEl = ET.SubElement( filesEl, "File" )

            filenameStr = os.path.basename( filename )
            ( fileBase, fileExt ) = os.path.splitext( filenameStr )
            filePath = os.path.dirname( filename )
            absFilename = os.path.abspath( filename )
            relFilename = os.path.relpath( absFilename, projectDir )

            fileNameEl = ET.SubElement( fileEl, "FileName" )
            fileNameEl.text = filenameStr

            fileTypeEl = ET.SubElement( fileEl, "FileType" )
            if filename.endswith( ".cpp" ):
                fileTypeEl.text = "8"
                objFile = "{0}/{1}.o".format( args.build, fileBase )
                depFile = "{0}/{1}.d".format( args.build, fileBase )
                linkObjList.append( objFile )
                genMake.write( "{0}: ${1}\n".format( depFile, filename ) )
                genMake.write( "\t{0}".format( cppDependRuleStr ) )
                genMake.write( "\tsed -ibk -e s'/C://' {0}\n".format( depFile ) )
                genMake.write( "-include {0}\n".format( depFile ) )
                genMake.write( "{0}: {2}\n".format( objFile, fileBase, filename ) )
                genMake.write( "\t{0}\n".format( cppRuleStr ) )
            elif filename.endswith( ".h" ):
                fileTypeEl.text = "5"
            elif filename.endswith( ".c" ):
                fileTypeEl.text = "1"
                objFile = "{0}/{1}.o".format( args.build, fileBase )
                depFile = "{0}/{1}.d".format( args.build, fileBase )
                linkObjList.append( objFile )
                genMake.write( "{0}: ${1}\n".format( depFile, filename ) )
                genMake.write( "\t{0}".format( cDependRuleStr ) )
                genMake.write( "\tsed -ibk -e s'/C://' {0}\n".format( depFile ) )
                genMake.write( "-include {0}\n".format( depFile ) )
                genMake.write( "{0}: {2}\n".format( objFile, fileBase, filename ) )
                genMake.write( "\t{0}\n".format( cRuleStr ) )
            elif filename.endswith( ".asm" ) or filename.endswith( ".s" ):
                fileTypeEl.text = "2"
                objFile = "{0}/{1}.o".format( args.build, fileBase )
                linkObjList.append( objFile )
                genMake.write( "{0}: {2}\n".format( objFile, fileBase, filename ) )
                genMake.write( "\t{0}\n".format( asmRuleStr ) )
            elif filename.endswith( ".lib" ):
                fileTypeEl.text = "4"
                linkObjList.append( filename )
            else:
                fileTypeEl.text = "5"  # "Text document" file type

            filePathEl = ET.SubElement( fileEl, "FilePath" )
            filePathEl.text = relFilename

# Write the final output files
#  Keil requires the xml declaration. Unfortunately Python 2.7 ignores xml_declaration=True, but it is possible to
#  force it to output the xml declaration anyway by setting encoding='UTF-8' (thanks Stack Overflow!)
projTree.write( args.output, encoding='UTF-8', xml_declaration=True )

# generate the makefile for building the axf file
objListStr = " ".join( linkObjList )
mapFileName = "{0}/{1}.map".format( args.build, targetName )
axfFileName = "{0}/{1}.axf".format( args.build, targetName )
genMake.write( "{0}: {1}\n".format( axfFileName, objListStr ) )
genMake.write( "\t$(ARM_LD) $(ARM_LDFLAGS) {0} --scatter {1} --list {2} -o {3}".format( objListStr, args.scatter, mapFileName, axfFileName ) )

getMakeFileObj = open( os.path.splitext( args.output )[ 0 ] + ".mk", "w" )
getMakeFileObj.write( "## File auto-generated by \"{0}\"\n".format( os.path.abspath( __file__ ) ) )
getMakeFileObj.write( "## Do not edit by hand.\n\n" )
getMakeFileObj.write( genMake.getvalue() )
