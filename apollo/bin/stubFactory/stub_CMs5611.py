import sys
from genStubs import *

stub = Stubs( "CMs5611", sys.argv[1], sys.argv[2] )

stub.include( "CMs5611.h" )
stub.newline()

stub.externC()
stub.newline()

stub.useNamespace( "airware::drivers" )
stub.newline()

stub.stubConstructor( "CMs5611", "void", "m_sens( 0 )", "m_off( 0 )", "m_tcs( 0 )", "m_tco( 0 )", "m_tref( 0 )", "m_tempsens( 0 )" )

stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::init", "SpiDrvDeviceCfg_t*" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::readTempPres", "int32_t*", "int32_t*" )

# unused stubs
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::startTemperatureReading" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::startPressureReading" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::endTemperatureReading" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::endPressureReading" )

stub.stubFunction( ("void",), "CMs5611::getCalibratedTempPress", "int32_t*", "int32_t*")

stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::resetSensor" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::readCoeff" )

stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "CMs5611::readADC", "uint32_t*" )

stub.stubFunction( ("void",), "CMs5611::delay50ns" )
