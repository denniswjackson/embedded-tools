import sys
from genStubs import *

stub = Stubs( "psbBsp", sys.argv[1], sys.argv[2] )

stub.include("psb/psbBsp.h")
stub.include("spi_drv_stm32.h")
stub.newline()

stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "readAirSpeedData", "SAirSpeedData_t*" )
