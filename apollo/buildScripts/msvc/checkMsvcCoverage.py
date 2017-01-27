# This script imports a visual studio coverage report (xml format), and checks to see if the coverage threshold is met
__author__ = 'jstevenson'

import argparse
import xml.etree.ElementTree as ET

# Get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', required='true', help="MSVC coverage report in xml format" )
parser.add_argument('--threshold', required='true', help="Line coverage threshold, as a decimal number ~ [0.0,100.0]" )
args = parser.parse_args()

## Load XML input tree
tree = ET.parse( args.input )
root = tree.getroot()

# Find all elements which source files and groups should be added to
modules = root.find('modules')
module = modules.find('module')

# 'line_coverage' does not count "partially covered" lines so it is more equivalent to gcov's "branch coverage"
# Instead, only find the percentage of "not covered" lines
linesCovered     = float(module.attrib['lines_covered'])
linesPartCovered = float(module.attrib['lines_partially_covered'])
linesNotCovered  = float(module.attrib['lines_not_covered'])
lineCoverage = ( 1.0 - ( linesNotCovered / ( linesCovered + linesPartCovered + linesNotCovered ) ) ) * 100.0

print "##teamcity[buildStatisticValue key='Line coverage threshold (percent)' value='{0:0.2f}']".format(float(args.threshold))
print "##teamcity[buildStatisticValue key='Line coverage (percent)' value='{0:0.2f}']".format(lineCoverage)

# Check against threshold
if lineCoverage < float(args.threshold):
    print "Fail: Line coverage of " + str(lineCoverage) + "% less than threshold of " + args.threshold + "%"
    exit(1)
else:
    print "Line coverage: " +  str(lineCoverage) + "%"
