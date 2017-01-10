import sys
from genStubs import *

stub = Stubs( "flash", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "stm32f4xx_flash.h" )

### Used Namespaces
stub.newline()

stub.externC()
stub.stubFunction( ("void",), "FLASH_Unlock" )
stub.stubFunction( ("void",), "FLASH_Lock" )
stub.stubFunction( ("FLASH_Status", "FLASH_COMPLETE"), "FLASH_ProgramByte", "uint32_t", "uint8_t" )
stub.stubFunction( ("FLASH_Status", "FLASH_COMPLETE"), "FLASH_ProgramWord", "uint32_t", "uint32_t" )
stub.stubFunction( ("FLASH_Status", "FLASH_COMPLETE"), "FLASH_EraseSector", "uint32_t", "uint8_t" )
stub.stubFunction( ("void",), "FLASH_ClearFlag", "uint32_t" )

stub.stubFunction( ("FlagStatus", "RESET"), "FLASH_OB_GetRDP" )