# This tool outputs a sorted list of files and other settings from a uvprojx, for use in diffing against another uvprojx
__author__ = 'jstevenson'

import argparse
import xml.etree.ElementTree as ET

# Get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', required='true', help="Input *.uvprojx file")
args = parser.parse_args()

## Load XML tree from both templates
projTree = ET.parse( args.input )
projRoot = projTree.getroot()

# Misc settings
print "Target Name: " + projRoot.find('./Targets/Target/TargetName').text
print "Build Dir: " + projRoot.find('./Targets/Target/TargetOption/TargetCommonOption/OutputDirectory').text
print "Output hex: " + projRoot.find('./Targets/Target/TargetOption/TargetCommonOption/OutputName').text
print "Output Dir: " + projRoot.find('./Targets/Target/TargetOption/TargetCommonOption/ListingPath').text

# Paths, defines, etc
includePaths = projRoot.find('./Targets/Target/TargetOption/TargetArmAds/Cads/VariousControls/IncludePath').text
sortedPaths = sorted( includePaths.split(';') )
for iPath in sortedPaths:
    print "-I: " + iPath

cppDefines = projRoot.find('./Targets/Target/TargetOption/TargetArmAds/Cads/VariousControls/Define').text
if cppDefines:
    sortedCppDefines = sorted( cppDefines.split() )
    for cppDef in sortedCppDefines:
        print "-D: " + cppDef

asmDefines = projRoot.find('./Targets/Target/TargetOption/TargetArmAds/Aads/VariousControls/Define').text
if asmDefines:
    sortedAsmDefines = sorted( asmDefines.split() )
    for asmDef in sortedAsmDefines:
        print "--asm: " + asmDef

# Only print files from one set of groups (don't print every file 2x if there is a hilsim target)
filenames = []
groups = projRoot.find('./Targets/Target/Groups')
for fileEl in groups.findall('./Group/Files/File'):
    filenames.append( fileEl.find('FilePath').text )

for fname in sorted(filenames):
    print fname