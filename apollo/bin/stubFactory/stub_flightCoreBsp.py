import sys
from genStubs import *

stub = Stubs( "flightCoreBsp", sys.argv[1], sys.argv[2] )

stub.include("flightCore/flightCoreBsp.h")
stub.include("bsp_spi.h")
stub.newline()

stub.stubFunction( ("bool","true"), "BSP_initBusMonitor", "const PowerBusMonitor_t", "const PowerBusCalibration_t", "ina2xxError_t *" )
stub.stubFunction( ("float","0.0F"), "BSP_getSupplyVoltage", "const PowerBusMonitor_t", "ina2xxError_t *" )
stub.stubFunction( ("float","0.0F"), "BSP_getSupplyCurrent", "const PowerBusMonitor_t", "ina2xxError_t *" )
stub.stubFunction( ("float","0.0F"), "BSP_getSupplyPower", "const PowerBusMonitor_t", "ina2xxError_t *" )

stub.stubFunction( ("bool","true"), "BSP_turnOnScr1" )
stub.stubFunction( ("bool","true"), "BSP_turnOnScr2" )
stub.stubFunction( ("bool","true"), "BSP_turnOnPldPwr" )
stub.stubFunction( ("bool","true"), "BSP_turnOnVBatt" )

stub.stubFunction( ("CircuitState_CircuitStatus","CircuitState_CircuitStatus_ON"), "BSP_getScr1BusState" )
stub.stubFunction( ("CircuitState_CircuitStatus","CircuitState_CircuitStatus_ON"), "BSP_getScr2BusState" )
stub.stubFunction( ("CircuitState_CircuitStatus","CircuitState_CircuitStatus_ON"), "BSP_getPldBusState" )

stub.stubFunction( ("bool","true"), "BSP_turnOffScr1" )
stub.stubFunction( ("bool","true"), "BSP_turnOffScr2" )
stub.stubFunction( ("bool","true"), "BSP_turnOffPldPwr" )
stub.stubFunction( ("bool","true"), "BSP_turnOffVBatt" )

stub.stubFunction( ("bool","true"), "BSP_isPldVoltagePresent" )
stub.stubFunction( ("void", ""), "BSP_turnOnPldCanTransceiver" )

stub.stubFunction( ("SpiDrvDeviceCfg_t*","NULL"), "bspGetSpiDeviceCfg", "SpiDev_t" )

stub.stubFunction( ("void",), "BSP_initLatencyMeasurement" )
stub.stubFunction( ("void",), "BSP_measureLatency" )