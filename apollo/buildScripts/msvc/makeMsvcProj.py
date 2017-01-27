# This script constructs visual studio "project.vcxproj" and "project.vcxproj.filters" files based on input "project.in.vcxproj" and "project.in.vcxproj.filters" templates
__author__ = 'jstevenson'

import argparse
import os
import xml.etree.ElementTree as ET

# Get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--template', required='true', help="The location and base name of project file templates")
parser.add_argument('--output', required='true', help="The location and name of project file (without extension)")
parser.add_argument('-I', help="Include paths, relative to current working directory" )
parser.add_argument('-D', help="All preprocessor directives, separated by whitespace, no \';\' required" )
parser.add_argument('--group', action='append', help="A group of source files or libraries in format \"groupName file1 file2, ... fileN\" paths are relative to current working directory" )
parser.add_argument('--prop', action='append', help="An MSVC property page whose settings this project shall inherit" )
args = parser.parse_args()

## Load XML tree from both templates
# Need to set this first, otherwise output will have a bunch of "ns0:" in it (ref http://stackoverflow.com/questions/8983041/saving-xml-files-using-elementtree)
MSVC_NS = 'http://schemas.microsoft.com/developer/msbuild/2003'
ET.register_namespace('', MSVC_NS )
ns = {'ns': MSVC_NS }
projTree = ET.parse( args.template + '.vcxproj' )
projRoot = projTree.getroot()
filterTree = ET.parse( args.template + '.vcxproj.filters' )
filterRoot = filterTree.getroot()

# Construct visual studio-style include path field
includePaths = ""
if args.I:
    for incPath in args.I.split():
        includePaths = includePaths + os.path.abspath( incPath ) + ";"

# Construct visual studio style pre-processor definitions field
compileTimeDefinitions = ""
if args.D:
    for compileTimeDefinition in args.D.split():
        compileTimeDefinitions = compileTimeDefinitions + compileTimeDefinition + ";"

#Set output name
for configuration in projRoot.findall('./ns:PropertyGroup/ns:TargetName',ns):
    configuration.text = os.path.basename( args.output )

# Add include paths to all build configurations
for configuration in projRoot.findall('./ns:ItemDefinitionGroup/ns:ClCompile/ns:AdditionalIncludeDirectories',ns):
    configuration.text = includePaths + configuration.text

# Add preprocessor definitions to all build configurations
for configuration in projRoot.findall('./ns:ItemDefinitionGroup/ns:ClCompile/ns:PreprocessorDefinitions',ns):
    configuration.text = compileTimeDefinitions + configuration.text

# Add pre-build step to all build configurations
for configuration in projRoot.findall('./ns:ItemDefinitionGroup/ns:PreBuildEvent/ns:Command',ns):
    configuration.text = os.path.abspath( args.output ) + '.out.bat'

# Find all elements which source files and groups should be added to
projItemGroups = projRoot.findall('./ns:ItemGroup',ns)
projSourceFiles = projItemGroups[1] # source files are placed in the second itemGroup in the project, lib files in the 3rd, and other files in the 4th
projLibFiles = projItemGroups[2]
projMiscFiles = projItemGroups[3]
filterItemGroups = filterRoot.findall('./ns:ItemGroup',ns)
filters = filterItemGroups[0] # Filters are defined in first item group, and the files in them are defined in the 2nd - 4th
filteredSourceFiles = filterItemGroups[1]
filteredLibFiles = filterItemGroups[2]
filteredMiscFiles = filterItemGroups[3]
uniqueId = 0 #Create dummy unique IDs which are unique to this file only

# Add property sheets
if args.prop:
    for prop in args.prop:
        propElement = ET.SubElement( projRoot, 'Import' )
        propElement.set('Project', os.path.abspath( prop ) )

# Add groups as "filters"
if args.group:
    for group in args.group:
        groupName = group.split()[0]
        filterElement = ET.SubElement( filters, "Filter" )
        filterElement.set('Include', groupName )
        uniqueIdElement = ET.SubElement( filterElement, "UniqueIdentifier" )
        uniqueIdElement.text = "{10899798-1248-4bc3-b3ed-00000000000" + str(uniqueId) + "}"
        uniqueId += 1

        # Add source and library files in the group to the project and the filter
        for filename in group.split()[1:]:
            entry = os.path.abspath( filename )
            if filename.endswith( ".lib" ):
                projItemEntry = ET.SubElement( projLibFiles, "Library" )
                filteredElement = ET.SubElement( filteredLibFiles, "Library" )
            elif filename.endswith( ".cpp" ) or filename.endswith( ".c" ):
                projItemEntry = ET.SubElement( projSourceFiles, "ClCompile" )
                filteredElement = ET.SubElement( filteredSourceFiles, "ClCompile" )
            elif filename.endswith( ".h" ):
                projItemEntry = ET.SubElement( projSourceFiles, "ClInclude" )
                filteredElement = ET.SubElement( filteredSourceFiles, "ClInclude" )
            elif filename.endswith( ".py" ):
                projItemEntry = ET.SubElement( projSourceFiles, "CustomBuild" )
                filteredElement = ET.SubElement( filteredSourceFiles, "CustomBuild" )
            else:
                projItemEntry = ET.SubElement( projMiscFiles, "None" )
                filteredElement = ET.SubElement( filteredMiscFiles, "None" )
            projItemEntry.set('Include', entry )
            filteredElement.set( 'Include', entry )
            filterElement = ET.SubElement( filteredElement, "Filter" )
            filterElement.text = groupName

# Write the final output files
projTree.write( args.output + '.out.vcxproj' )
filterTree.write( args.output + '.out.vcxproj.filters' )