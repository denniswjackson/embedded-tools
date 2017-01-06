#!/usr/bin/env python
'''
Extract ROM and RAM sizes from Keil map files.
Output is a TeamCity key-value pair for plotting stats
Digit extraction from http://stackoverflow.com/a/4289557/346

Airware M4 memory maps: http://confluence/pages/viewpage.action?pageId=6685368

@author Dennis W. Jackson <djackson@airware.com>
@date 2015-02-02
@copyright Copyright (c) 2015 Airware. All rights reserved.
'''

import argparse
import mmap
import os.path
import sys

__version__ = "1.2"

# lines in the map file that correspond to the data we want
RAM_TEXT = "Total RW  Size (RW Data + ZI Data)"
ROM_TEXT = "Total ROM Size (Code + RO Data + RW Data)"


def find_memory_usage(filename, options):
    '''
    Access Keil memory map file as a memory mapped object and extract the total
    RAM and ROM usage.
    '''
    h_file = open(filename)
    search_str = mmap.mmap(h_file.fileno(), 0, access=mmap.ACCESS_READ)

    ram_idx = search_str.find(RAM_TEXT)
    rom_idx = search_str.find(ROM_TEXT)

    if ram_idx != -1:
        search_str.seek(ram_idx)
        ram_string = search_str.readline()
        print_stats("RAM", ram_string, options.ram, options.moduleName)

    if rom_idx != -1:
        search_str.seek(rom_idx)
        rom_string = search_str.readline()
        print_stats("ROM", rom_string, options.rom, options.moduleName)


def print_stats(type_str, stats_str, max_memory_kilobytes, module_name):
    '''
    Report total usage in bytes and percentage for the given memory type
    @param type_str RAM or ROM
    @param stats_str The line of text from the map file with the values to extract
    @param max_memory_kilobytes Maximum amount (in KB) of the memory type for this module
    @param module_name Name of the module being analyzed
    '''
    size = [int(x) for x in stats_str.split() if x.isdigit()]
    size_bytes = size[0]
    max_memory_bytes = int(max_memory_kilobytes) * 1024
    size_percent = 100.0 * (size_bytes / float(max_memory_bytes))
    print "##teamcity[buildStatisticValue key='{1} {0} size (bytes)' value='{2}']".format(type_str, module_name, size_bytes)
    print "##teamcity[buildStatisticValue key='{1} {0} max size (bytes)' value='{2}']".format(type_str, module_name, max_memory_bytes)
    print "##teamcity[buildStatisticValue key='{1} {0} usage (percent)' value='{2:0.2f}']".format(type_str, module_name, size_percent)


def main():
    '''
    Main - configure parser and handle input
    '''
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s (version {0})".format(__version__))
    parser.add_argument("mapfile", help="Keil memory map to parse")
    parser.add_argument("--ram", help="Maximum RAM available (in KB) (SCAP = 768, Sats = 192)",
                        default=192)
    parser.add_argument("--rom", help="Maximum ROM available (in KB) (SCAP = 1728, Sats = 704)",
                        default=704)
    parser.add_argument("-m", "--moduleName", default="", help="Name of module to use in output")
    args = parser.parse_args()

    if len(sys.argv) > 1:
        # use the filename as the module name if it is not specified
        if args.moduleName == "":
            args.moduleName = os.path.splitext(os.path.basename(args.mapfile))[0]

        find_memory_usage(args.mapfile, args)


if __name__ == "__main__":
    main()
