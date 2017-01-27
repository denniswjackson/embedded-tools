"""
@brief      Module to generate bootloader-compliant image headers
@file       makeImageHeader.py
@author     Jeeves
@copyright  Copyright (c) 2016 Airware. All rights reserved.
@date       Oct 3, 2016
"""

from cStringIO import StringIO
from intelhex import IntelHex
from crcmod.predefined import mkCrcFun
import struct
import sys
import argparse
from os.path import exists

__author__ = 'jreeves'

# excluding the CRC field at the end of the header for CRC calculation simplicity
HEADER_STRUCT = struct.Struct(
	'<' # little endian
	'I' # magic: unsigned int
	'I' # image size: unsigned int, units of bytes NOT including header
	'I' # image version: unsigned int, major.minor.patch
	'I' # build number: unsigned int
	'I' # code start address
	'I')# jump addr: unsigned int, address byte offset

# full header size including CRC16 at the end
HEADER_SIZE_BYTES = HEADER_STRUCT.size + 2

# magic image indicator
HEADER_MAGIC = ( ( ord( 'A' ) << 24 ) | \
                 ( ord( 'W' ) << 16 ) | \
                 ( ord( 'F' ) << 8 ) | \
                 ( ord( 'W' ) << 0 ) )

CRC_TYPE = 'modbus'

# From the STM32F4 cortex-M4 programmer's reference manual:
# "When setting TBLOFF, you must align the offset to the number of exception
# entries in the vector table. The minimum alignment is 128 words. Table
# alignment requirements mean that bits[8:0] of the table offset are always
# zero"
IMG_ALIGNMENT_BYTE_COUNT = 512
IMG_BASE_ALIGNMENT_MASK = ~((1 << IMG_ALIGNMENT_BYTE_COUNT) - 1)

def make_image_header(in_file, ver_int, build, img_base, start_addr, out_file):
    """
    Builds a header for an application image and prepends it (in place) to the hex file

    :param in_file: name of intel hex input file (will also be the output file)
    :type in_file: str
    :param ver_int: the integer formatted version of the image (major.minor.patch)
    :type ver_int: int
    :param build: the integer build number
    :type build: int
    :param img_base: the base address of the image (where the header will go)
    :type img_base: int
    :param start_addr: a jump address to use (if different from img_base). If 'None', img_base will be used
    :type start_addr: int
    :param out_file: an output file to write (if different from in_file). If 'None', header will be added in place
    :type out_file: str
    :return: None
    """

    # inspect the hex file for ranges
    ih = IntelHex(in_file)
    hex_start = ih.minaddr()
    hex_end = ih.maxaddr()
    image_size = hex_end - hex_start + 1;

    # parameter fix-up
    if start_addr is None:
    	start_addr = hex_start
    if out_file is None:
    	out_file = in_file

    # sanity check: if the hex_start is the same as the sector base, a header
    # has probably already been added. Abort
    if (hex_start == img_base):
        raise ValueError('hex start and sector base are the same, adding a header would corrupt the image')

    # make sure the main image is properly aligned to meet the vector table requirements
    if (hex_start & IMG_BASE_ALIGNMENT_MASK) != 0:
    	raise ValueError('image base address {0} is not aligned to a {1} byte value'.format(hex_start, IMG_ALIGNMENT_BYTE_COUNT))

    # make sure the header fits
    if (img_base + HEADER_SIZE_BYTES > hex_start):
    	raise ValueError('not enough space between the image base ({0}) and start of code ({1})'.format(hex(img_base), hex(hex_start)))

    # Make sure the jump location is valid
    if (start_addr < hex_start) or (start_addr > hex_end):
    	raise ValueError('invalid jump address specified')

    # Convert hex to bin
    sio = StringIO()
    ih.tobinfile(sio)

    # get CRC of the main image
    crc_result = mkCrcFun(CRC_TYPE)(sio.getvalue())

    # build the header without the CRC and include it in the CRC calculation from above
    header = HEADER_STRUCT.pack(HEADER_MAGIC, image_size, ver_int, build, hex_start, start_addr)
    crc_result = mkCrcFun(CRC_TYPE)(header, crc=crc_result)

    # final CRC result
    print('crc_result = {0}'.format(hex( crc_result )))

    # insert header at the start of the image
    ih.puts(img_base, header)

    # insert the crc field at the end
    ih.puts(img_base + HEADER_STRUCT.size, struct.pack('<H', crc_result))
    ih.tofile(out_file, format='hex')
    sio.close()

def bcd(ival):
    """
    Convert an integer into a binary coded decimal form (for example 15 becomes 21 or 0x15)

    :param ival: the input
    :type ival: int
    :return: BCD version of ival
    """

    val_arr = []
    while (ival != 0):
	    dig = ival % 10
	    val_arr.insert(0, dig)
	    ival = int(ival/10)

    ret_val = 0
    nib = 0
    for val in reversed(val_arr):
        ret_val = ret_val | val << nib
        nib = nib + 4
    return ret_val

def get_sector_base(sector_type, arch_str):
    """
    Get the sector base address given sector type and architecture

    We support exactly two sector types for this script: app, and bs2
    We support exactly two architecture types: F40x and F42x as these are the
    only STM32 architectures with known memory maps in Airware products. Note
    that we allow promiscuous formatting of the arch string. It can be upper or
    lower or mixed case and may have other characters. For example STM32F40x will
    succeed as will stm32F405.

    :param sector_type: name of the sector type (e.g. app or bs2)
    :type sector_type: str
    :param arch_str: the architecture string (e.g. stm32f40x)
    :type arch_str: str
    """
    addr_table = {'app': {'40x': 0x08010000, '42x': 0x08010000}, \
                  'bs2': {'40x': 0x080C0000, '42x': 0x081C0000}}
    # we allow promiscuous formatting for the arch_str. Do some cleanup and
    # figure out what's being requested
    arch_str = arch_str.lower()
    if 'f42' in arch_str:
        key = '42x'
    elif 'f40' in arch_str:
        key = '40x'
    else:
        raise ValueError('unknown architecture {0}'.format(arch_str))

    return addr_table[sector_type.lower()][key]


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', required=True, help="Either the version file containing the FW version or the version string itself")
    parser.add_argument('-b', '--build', required=False, type=int, help="The build number")
    parser.add_argument('-a', '--arch', required=True, help="The target STM architecture definition (e.g. STM32F40x or STM32F427_437xx)")
    parser.add_argument('-s', '--sector', required=True, help="The target sector (e.g. app or bs2)")
    parser.add_argument('-j', '--start', required=False, help="The start address to jump to")
    parser.add_argument('-o', '--output', required=False, help="Optional output file (if in-place header creation is not desired)")
    parser.add_argument('file', help='The hex file to prepend the header to')
    args = parser.parse_args()

    # if the version string contains "VERSION", it's the path to the version file.
    # otherwise treat it as the version string itself
    ver_str = args.version
    if 'VERSION' in args.version:
        # read the version file and convert it to its final BCD form
        ver_str = open(args.version).read()

    (mjr, mnr, pat) = ver_str.split('.')
    ver_int = (bcd(int(mjr))<<24) | (bcd(int(mnr))<<16) | (bcd(int(pat))<<8)

    # sanity check that the file exists
    if not exists(args.file):
    	raise ValueError('file {0} does not exist!'.format(args.file))

    # get the sector base address from the architecture and sector type info
    sector_addr = get_sector_base(args.sector, args.arch)
    make_image_header(args.file, ver_int, args.build, sector_addr, args.start, args.output)
