import sys
from genStubs import *

stub = Stubs( "gpsBsp", sys.argv[1], sys.argv[2] )

stub.include("gps/gpsBsp.h")
stub.include("bsp_spi.h")
stub.newline()

stub.stubFunction( ("bool","true"), "BSP_OSInit" )
stub.stubFunction( ("BSP_BctErr_t","BCT_ERR_NONE"), "BSP_Init" )

stub.stubFunction( ("SpiDrvErr_t","SPI_DRV_ERR_NONE"), "spiDrvPollRead16", "SpiDrvDeviceCfg_t *", "uint16_t *" )
stub.stubFunction( ("SpiDrvDeviceCfg_t*","NULL"), "bspGetSpiDeviceCfg", "SpiDev_t" )

stub.stubFunction( ("void",""), "BSP_GPS_Reset", "uint8_t" )
stub.stubFunction( ("CPUTemperatureErr_t","CPU_TEMPERATURE_ERR_NONE"), "BSP_GetOutsideAirTemperature_K", "float * const" )