import sys
from genStubs import *

stub = Stubs( "gnssBsp", sys.argv[1], sys.argv[2] )

stub.include("gnss/gnssBsp.h")
stub.newline()

stub.stubFunction( ("BSP_BctErr_t","BCT_ERR_NONE"), "BSP_Init" )
stub.stubFunction( ("bool","true"), "BSP_OSInit" )
stub.stubFunction( ("bool","true"), "BSP_initNeoM8Uart" )
stub.stubFunction( ("SCommonDrvPin_t *","&SCommonDrvPin_t()"), "BSP_getNeoM8ResetPin" )
stub.stubFunction( ("bool","true"), "BSP_enableNeoM8TimePulse", "BSP_FNCT_ISR" )
stub.stubFunction( ("void",), "BSP_gpsReset", "bool" )
stub.stubFunction( ("bool","false"), "BSP_readNeoM8TimePulse" )
stub.stubFunction( ("bool","false"), "BSP_readRm3100Drdy" )
stub.stubFunction( ("SpiDrvDeviceCfg_t*","&SpiDrvDeviceCfg_t()"), "bspGetSpiDeviceCfg", "SpiDev_t" )