##
#
# @brief      Module to generate OTP hex images for manufacturing
# @file       makeOTPHex.py
# @author     Jeeves
# @copyright  Copyright (c) 2015-2016 Airware. All rights reserved.
# @date       August 21, 2015
#

import sys
import os
import argparse
import struct
import math
import datetime
import systemmessages.STM32OTPParams_pb2 as OTP

from intelhex import IntelHex
from cStringIO import StringIO
from datetime import date

__version__ = "0.2.0"

##
#
# @brief Some key constants
#

#  MAC address-related constants. Please refer to
# http://confluence/display/AIR/MAC+Address+Assignments+for+Internal+Use
# for details
MAC_ADDRESS_MAX_ASCII_CHAR_COUNT = 12 # 6 hex values (2 chars each)
MAC_ADDRESS_OUI_ASCII_CHAR_COUNT = 6  # 3 hex values (2 chars each)
MAC_ADDRESS_BOARD_ID_ASCII_CHAR_COUNT = MAC_ADDRESS_MAX_ASCII_CHAR_COUNT - MAC_ADDRESS_OUI_ASCII_CHAR_COUNT
MAC_ADDRESS_ASCII_OUI_AIRWARE = "E4C62B" # constant, IEEE assigned Airware OUI

# from the STM32F4x reference manual (RM-0090):
OTP_DATA_BASE_ADDRESS = 0x1FFF7800
OTP_SIZE_BYTES = 512
OTP_LOCK_BASE_ADDRESS = OTP_DATA_BASE_ADDRESS + OTP_SIZE_BYTES
OTP_BLOCK_SIZE_BYTES = 32

# founding year of unmanned innovation:
MIN_MFG_YEAR = 2011

# http://confluence/display/AIR/Production+Parameters+and+Test+Lifecycle+Data+Board+ICD#ProductionParametersandTestLifecycleDataBoardICD-ProductIDtoProductTypeMappingTableforAirware(VID0x0001)
SUPPORTED_PRODUCT_TYPES = [
    'Flight Core',
    'Autopilot Processor',
    'Peripheral Interface Board',
    'Application Core',
    'Ground Datalink Module',
    'Airspeed Module',
    'GPS Module',
    'Actuator Control Module',
    'Air Datalink Module',
    'AGL Module',
    'Ground Datalink Module',
    'Security'
]


def verify_product_type( product_type ):
    """
    @brief  verifies that the passed in product type is supported by Airware
    @param  product_type product type to verify 
    @return True if valid, False if invalid
    """
    return product_type in SUPPORTED_PRODUCT_TYPES

def range_check_unsigned( uintVal, maxByteCount ):
    """
    @brief  Check that an unsigned value fits in a specified number of bytes
    @param  uintVal      The value to check
    @param  maxByteCount The max number of bytes the parameter can occupy
    @return True if it fits, False if it doesn't.

    """
    maxVal = ( 1 << (maxByteCount*8) ) - 1
    return ( uintVal > 0 ) and ( uintVal <= maxVal )


def validate_hw_rev( hwRev ):
    """
    @brief  Check that hwRev value passed is valid
    @param  hwRev      The hwRev string to check
    @return True if it's valid, False if it's not
    """
    if len( hwRev ) != OTP.BYTE_COUNT_HW_REV:
        print "hwRev must have length of exactly " + str( OTP.BYTE_COUNT_HW_REV )
        return False

    if not hwRev.isalnum():
        print "hwRev can only be 0...9 or A...Z"
        return False

    if hwRev.isalpha() and ( not hwRev.isupper() ):
        print "hwRev must be uppercase"
        return False

    return True

def validate_key_name( keyName ):
    """
    @brief  Check that keyName value passed is valid
    @param  keyName      The keyName string to check
    @return True if it's valid, False if it's not
    """
    if len( keyName ) >= OTP.BYTE_COUNT_RECOVERY_SIG_NAME:
        print "keyName must have length of strictly less than " + str( OTP.BYTE_COUNT_RECOVERY_SIG_NAME )
        return False

    if keyName[0] != 's':
        print "only signature keys accepted, first letter should be \'s\'"
        return False

    if not keyName[2].isdigit():
        print "key number (in the key name string) is not valid. Example: s01FwDv, sT1FwRk. Your string: " + keyName
        return False

    if keyName[3:5] != "Fw":
        print "only firmware keys should be used for recovery keys."
        return False

    if not ( keyName[5:7] == "Pr" or keyName[5:7] == "Dv" or keyName[5:7] == "Rk" ):
        print "only acceptable key name suffixes are \'Pr\' for production, \'Dv\' for development, and \'Rk\' for recovery keys."
        return False
 
    if not keyName.isalnum():
        print "key name can only contain 0...9 or A...Z"
        return False

    return True

def validate_serial_number( sn, hwRev ):
    """
    @brief  Check that the serial number string passed is valid
    @param  sn      The serial number string to check
    @param  hwRev   The validated hwRev string passed to the script (i.e.
                    uppercase, alphanumeric).
    @return True if it's valid, False if it's not
    """

    if len( sn ) != OTP.BYTE_COUNT_SERIAL_NUMBER:
        print "serial number string must be exactly " + str( OTP.BYTE_COUNT_SERIAL_NUMBER ) + " characters."
        return False

    baseLen = OTP.BYTE_COUNT_SERIAL_NUMBER - 1
    if not sn[ 0 : baseLen ].isdigit():
        print 'first %d characters of serial number must be stricly numeric' % baseLen
        return False

    if sn[ baseLen] != hwRev:
        print 'last character of serial number must match hardware revision'
        return False

    return True

def get_key_modulus( keyPath ):
    """
    @brief   Get the RSA 2048 "modulus" (256-byte binary key) from an openssl
             public key file.
    @note    The expectation is that these key files are fetched from the HSM
             using the "getKeyFile" command and asking for the associated .pub
             file. Refer to:
             http://confluence/display/ENG/Cryptographic+Services+and+Key+Information+Used+in+Airware+Products
             for details on this procedure.
    @param   keyPath  filesystem path to the public key file
    @return  a 256-byte binary string with the key data
    """
    modPath = keyPath + ".mod"
    os.system( "openssl rsa -in " + keyPath + " -modulus -pubin -noout -out " + modPath )
    with open( modPath, "r" ) as modFile:
        modStrData = modFile.read()
        modStrData = modStrData.split("=")
        modStrData = modStrData[1].strip()
        strBytes = [ modStrData[ i : i+2 ] for i in range( 0, len( modStrData ), 2 ) ]
        modData = ''.join([ chr(int( byte, 16 ) ) for byte in strBytes ] )

        # sanity check that modData is the right size:
        if len(modData) != OTP.BYTE_COUNT_RECOVERY_SIG_DATA:
            print "Key is the wrong size. Should be 256 bytes (RSA 2048 bit key)"
            exit(-1)

        # return tuple to facilitate expected vs read key comparison when reading from OTP
        return (modData, strBytes)

def set_lock_bytes( hexFile ):
    """
    @brief   Set the OTP lock bytes for blocks that have been written in a
             hex file
    @param   hexFile   The python IntelHex object containing the hex file data
    @details The STM32 reference manual specifies that OTP bytes in the normal
             512-byte region can be written arbitrarily many times until the
             "lock byte" for a given block is set, at which point any attempts
             to write to the block will result in a hardware write error. Note
             the additional implication that once an OTP block has *any* data
             in it, and is then programmed to the device using the hex file this
             module generates, that block is locked forever and can never have
             data added to it, even if it isn't maximally utilized.
             
             The lock bytes for each 32-byte block follow immediately after the
             OTP region and can thus be included in the hex file and thereby
             get programmed as one continuous operation. This function checks
             to see which blocks have valid data in them, and sets the
             corresponding lock byte if it does.
    """
    dataDict = hexFile.todict()
    blockShift = int( math.log( OTP_BLOCK_SIZE_BYTES, 2 ) )

    for key, value in dataDict.iteritems():
        blockIdx = ( int( key ) & ( OTP_SIZE_BYTES - 1 ) ) >> blockShift
        if value != 0xFF and hexFile[ OTP_LOCK_BASE_ADDRESS + blockIdx ] != 0:
            hexFile[ OTP_LOCK_BASE_ADDRESS + blockIdx ] = 0

def get_date_string( dateInput ):
    """
    @brief   Either validate an input date string, or create one from today's date
    @param   dateInput  The input date string (may be empty or None)
    @return  A correctly formatted (YYYYMMDD) date string
    """

    today = date.today()

    dateString = dateInput
    if not dateString:
        # set the mfg date to today
        dateString = str( today.year ) + "{:02d}".format( today.month ) + "{:02d}".format( today.day)

    # sanity check everything, even if we generated it ourselves (trust no one)
    if len( dateString ) != OTP.BYTE_COUNT_MFG_DATE:
        print "date string must be exactly " + str( OTP.BYTE_COUNT_MFG_DATE ) + " characters."
        exit( -1 )

    year = dateString[0:4]
    month = dateString[4:6]
    day = dateString[6:8]
    
    if int( year ) < MIN_MFG_YEAR:
        print "year specified is older than Airware."
        exit( -1 )
   
    # this will throw an exception if it's an invalid calendar date:
    dateCheck = datetime.datetime( int( year ), int( month ), int( day ) )

    return dateString

def get_mac_address( macInput ):
    """
    @brief    Convert an ASCII MAC address implementation to binary
    @param    macInput   The ASCII-hex MAC string (should be 6 or 12 ASCII characters
                         representing 3 or 6 bytes respectively).
    @return   the binary 6-byte string containing the bytes specified in macInput
    """

    if len( macInput ) != MAC_ADDRESS_BOARD_ID_ASCII_CHAR_COUNT and len( macInput ) != MAC_ADDRESS_MAX_ASCII_CHAR_COUNT:
        print "mac address must be either " + str( MAC_ADDRESS_BOARD_ID_ASCII_CHAR_COUNT ) + " or " + str( MAC_ADDRESS_MAX_ASCII_CHAR_COUNT ) + " characters in length."
        exit( -1 )

    if len( macInput ) == MAC_ADDRESS_BOARD_ID_ASCII_CHAR_COUNT:
        # prepend the Airware OUI:
        macInput = MAC_ADDRESS_ASCII_OUI_AIRWARE + macInput

    macPieces = [ macInput[ i : i + 2 ] for i in range( 0, len( macInput ), 2 ) ]
    macByteStr = ''.join( [ chr(int( byte, 16 ) ) for byte in macPieces ] )

    # sanity check our work
    if len( macByteStr ) != OTP.BYTE_COUNT_MAC:
        print "binary MAC address string must be exactly " + str( OTP.BYTE_COUNT_MAC ) + " characters."
        exit( -1 )

    return macByteStr


def format_variable_string( inputStr, maxLen ):
    """
    @brief   check and format a variable length NULL-terminated string
    @param   inputStr The unformatted string
    @param   maxLen The maximum length of the string buffer (including NULL terminator)
    @return  The formatted string
    @details In general NULL-terminated strings are variable-length fields. In
             order to make them easy to read from OTP, we zero pad them out to
             their maximum length (note that the default flash value is 0xFF).
             This also has the added benefit of ensuring that strings with max
             lengths which span multiple blocks get all of their blocks locked
             in OTP, regardless of whether all bytes are being used in the string
             itself. This is important for validating whether that parameter is
             present or not when firmware goes to check it.
    """

    # note the '=' sign. We still need room for the NULL-terminator
    if len( inputStr ) >= maxLen:
        print "string " + inputStr + " exceeds its maximum length of " + str( maxLen - 1 ) + " characters."
        exit( -1 )

    numZeros = maxLen - len( inputStr )
    return inputStr + '\0'*numZeros

def auto_int( x ):
    """
    @brief   Type conversion function to be used in argparse arguments that must
             support both decimal and hex
    @param   x  The string value to convert
    @return  The converted integer
    """
    try:
        n = int( x, 10 )
    except ValueError:
        try:
            n = int( x, 16 )
        except ValueError:
            print "Invalid string " + x + ". Only decimal and hex values supported for auto_int type"
            exit( -1 )
    return n

def main():
    """
    @brief  main routine
    """

    parser = argparse.ArgumentParser( description="Create a board-specific hex file to program the STM32's OTP flash memory." )

    parser.add_argument( "-r", "--hwRev",   action="store",
                         type=str, required=True,
            help="hardware revision. Single ASCII character (e.g. 0, 1, A, etc.)" )

    parser.add_argument( "-v", "--vid",     action="store",
            default = 1, type=auto_int, required=False,
            help="vendor ID, in decimal or hex, e.g. 0xXX" )

    parser.add_argument( "-p", "--pid",     action="store",
                         type=auto_int, required=True,
            help="product ID, in decimal or hex, e.g. 0xXX" )

    parser.add_argument( "-c", "--cid",     action="store",
                         type=auto_int, required=True,
            help="class ID, in decimal or hex, e.g. 0xXX" )

    parser.add_argument( "-t", "--type",    action="store",
                         type=str, required=True,
            help="product type string" )

    parser.add_argument( "-s", "--serial",  action="store",
                         type=str, required=True,
            help="serial number. Last character must match hwRev. See production parameters documentation for details." )

    parser.add_argument( "-m", "--mac",     action="store",
                         type=str, required=True,
            help="product MAC address as either a 6-character or 12-character ASCII hex string representing the bytes in the address (3 or 6 bytes respectively). If a 3-byte (6 character) version is passed, a 3-byte Airware prefix (E4C62B) will be prepended to make a complete 6-byte address that gets written to OTP." )

    parser.add_argument( "-d", "--date",    action="store",
                         type=str, required=False,
            help="manufacturing date (YYYYMMDD). If not specified, forced to today's date" )

    parser.add_argument( "-K", "--keyName", action="store",
                         type=str, required=True,
            help="7-byte string name to use for the key name. This should be the same string that gets passed to the HSM when executing the \"getKeyFile\" routine. (see also keyFile argument)" )

    parser.add_argument( "-k", "--keyFile", action="store",
                         type=str, required=True,
            help="path to the public key (.pub) file to use for the recovery key. This is expected to come from the HSM by executing the \"getKeyFile\" routine. Refer to the product cryptography confluence page for details." )

    parser.add_argument( "-o", "--outfile", action="store",
                         type=str, required=False,
            help="output file name" )

    parser.add_argument( "-V", "--version", action="version", version='%(prog)s ' + __version__ )


    args = parser.parse_args()

    # range and sanity checks:
    if not validate_hw_rev( args.hwRev ):
        print "hwRev validation failed."
        exit( -1 )

    if not range_check_unsigned( args.vid, OTP.BYTE_COUNT_VENDOR_ID ):
        print "vendor id range check failed."
        exit( -1 )

    if not range_check_unsigned( args.pid, OTP.BYTE_COUNT_PRODUCT_ID ):
        print "product id range check failed."
        exit( -1 )

    if not range_check_unsigned( args.cid, OTP.BYTE_COUNT_CLASS_ID ):
        print "class id range check failed."
        exit( -1 )

    if not validate_serial_number( args.serial, args.hwRev ):
        print "serial number validation failed."
        exit( -1 )

    if not verify_product_type( args.type ):
        print "product type validation failed."
        exit( -1 )

    if not validate_key_name( args.keyName ):
        print "recovery key name validation failed."
        exit( -1 )


    # checking/formatting of the date:
    dateString = get_date_string( args.date )

    # checking/formatting of MAC address:
    macString = get_mac_address( args.mac )

    # checking/formatting of productType string:
    productTypeString = format_variable_string( args.type, OTP.BYTE_COUNT_PRODUCT_TYPE )

    # formatting of the key name string:
    keyNameStr = format_variable_string( args.keyName, OTP.BYTE_COUNT_RECOVERY_SIG_NAME )

    ih = IntelHex()

    # hwRev
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_HW_REV, args.hwRev )

    # struct format string for the following 3 items is:
    # little endian 16-byte unsigned integer:
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_VENDOR_ID, struct.pack('<H', args.vid ) )
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_PRODUCT_ID, struct.pack('<H', args.pid ) )
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_CLASS_ID, struct.pack('<H', args.cid ))

    # serial number (not NULL terminated)
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_SERIAL_NUMBER, args.serial )

    # mac address
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_MAC, macString )

    # manufacture date:
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_MFG_DATE, dateString )


    # product type (NULL terminated and zero-padded out to the full size)
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_PRODUCT_TYPE, productTypeString )

    # recovery key name string
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_RECOVERY_SIG_NAME, keyNameStr )

    # recovery key data (public)
    # pick the binary stream of key data
    ih.puts( OTP_DATA_BASE_ADDRESS + OTP.BYTE_OFFSET_RECOVERY_SIG_DATA, get_key_modulus( args.keyFile )[0] )

    # set lock bytes for anything written
    set_lock_bytes( ih )

    # write the hex file to a string object
    sio = StringIO()
    ih.write_hex_file( sio )
    hexstr = sio.getvalue()
    sio.close()

    # write to either stdout or specified output file name
    if not args.outfile:
        print hexstr
    else:
        fio = open( args.outfile, 'w' )
        fio.write( hexstr )
        fio.close()
        print "hex file generated"


if __name__ == "__main__":
    main()
