import sys
from genStubs import *

stub = Stubs( "flashSectionStm32", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "flashSectionStm32.h" )

### Used Namespaces
stub.newline()

stub.externC()
stub.stubFunction( ("flashSectionErr_t", "FLASH_SECTION_ERR_NONE"), "flashSectionInit", "flashSectionType_t", "SFlashSection_t *" )
stub.stubFunction( ("flashSectionErr_t", "FLASH_SECTION_ERR_NONE"), "flashSectionGetUsableSize_WORDS", "const SFlashSection_t *", "size_t *" )
stub.stubFunction( ("flashSectionErr_t", "FLASH_SECTION_ERR_NONE"), "flashSectionGetStartAddress", "const SFlashSection_t *", "const uint32_t **" )
stub.stubFunction( ("flashSectionErr_t", "FLASH_SECTION_ERR_NONE"), "flashSectionVerify", "const SFlashSection_t *", "bool *" )
stub.stubFunction( ("flashSectionErr_t", "FLASH_SECTION_ERR_NONE"), "flashSectionIsWritable", "const SFlashSection_t *", "bool *" )
stub.stubFunction( ("flashSectionErr_t", "FLASH_SECTION_ERR_NONE"), "flashSectionErase", "const SFlashSection_t *" )
stub.stubFunction( ("flashSectionErr_t", "FLASH_SECTION_ERR_NONE"), "flashSectionFinalize", "const SFlashSection_t *" )
stub.stubFunction( ("flashSectionErr_t", "FLASH_SECTION_ERR_NONE"), "flashWriteWords", "const uint32_t *", "const uint32_t *", "size_t" )
