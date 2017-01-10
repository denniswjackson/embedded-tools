import sys
from genStubs import *

stub = Stubs( "hades", sys.argv[1], sys.argv[2] )

stub.include( "adcTemperature.h" )
stub.include( "BaseBsp.h" )
stub.include( "CMcp2515.h" )
stub.include( "CMs5611.h" )
stub.include( "i2c.h" )
stub.include( "mpu6000.h" )
stub.include( "timeDriverStm32.h" )
stub.newline()

stub.useNamespace( "airware::drivers"   )

stub.stubFunction( ("void",), "BSP_redLedOn" )
stub.stubFunction( ("void",), "BSP_redLedOff" )
stub.stubFunction( ("void",), "BSP_greenLedOn" )
stub.stubFunction( ("void",), "BSP_greenLedOff" )
stub.stubFunction( ("void",), "BSP_ReadUniqueId", "CPU_INT08U*", "size_t" )
stub.stubFunction( ("BSP_Err_t", "BSP_ERR_NONE"), "BSP_serialNumberToUniqueId", "const char *", "uint32_t *" )
stub.stubFunction( ("BSP_Err_t", "BSP_ERR_NONE"), "BSP_readMfgMem", "void *", "const uint32_t", "const uint32_t" )
stub.stubConstructor( "CCanStm32", "CanDrvMsg_t *, const size_t, CanDrvMsg_t *, const size_t" )
stub.stubDestructor( "CCanStm32" )
stub.addLine( "static CanDrvCfg_t s_dummyCan1;" )
stub.stubFunction( ("CanDrvCfg_t*", "&s_dummyCan1"), "CCanStm32::getCanDrvCfg" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "canDrvEnabledStdRx", "CanDrvCfg_t *const", "CanRxCallback_t" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CCanStm32::send", "CanDrvMsg_t*" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CCanStm32::receive", "CanDrvMsg_t*" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CCanStm32::sendBlocking", "CanDrvMsg_t*", "unsigned short" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CCanStm32::receiveBlocking", "CanDrvMsg_t*", "unsigned short" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CCanStm32::init" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "canDrvTransmitStdBlock", "CanDrvCfg_t *const", "CanTxMsg*", "CanDrvTxMbox_t", "uint16_t", "bool" )
stub.stubFunction( ("void", ""), "canDrvSetBridging", "uint32_t", "uint32_t" )

stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CMcp2515::registerEventCallback", "Mcp2515_EventCallback_t" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CMcp2515::enableEventReport", "uint32_t" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CMcp2515::process", "uint16_t" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CMcp2515::send", "CanDrvMsg_t*" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CMcp2515::sendBlocking", "CanDrvMsg_t *", "uint16_t" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CMcp2515::receive", "CanDrvMsg_t *" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "CMcp2515::receiveBlocking", "CanDrvMsg_t *", "uint16_t" )
stub.stubConstFunction( ("Mcp2515_State_t", "MCP2515_STATE_RUNNING"), "CMcp2515::getState" )

stub.stubFunction( ("BSP_BctErr_t", "BCT_ERR_NONE"), "BSP_BaseInit" )
stub.stubFunction( ("CanDrvErr_t", "CAN_DRV_ERR_NONE"), "BSP_BaseOSInit" )



#### Constructors/Destructors
stub.stubConstructor( "CMcp2515", "" )

# Singletons
stub.addLine( "CMcp2515 &CMcp2515::theMcp2515()      " )
stub.addLine( "{                          " )
stub.addLine( "    static CMcp2515 s_CMcp2515;" )
stub.addLine( "    return s_CMcp2515;       " )
stub.addLine( "}                          " )
stub.newline()

stub.addLine( "CCanStm32  BSP_can1( NULL, 0, NULL, 0);" )
stub.addLine( "CCanStm32  BSP_can2( NULL, 0, NULL, 0);" )
stub.newline()

# Everything after this call is extern "C"ed
stub.externC()
stub.include( "serial.h" )
stub.include( "string.h" )
stub.stubFunction( ("CPU_BOOLEAN", "DEF_TRUE"), "BSP_HwAddr_Set", "const CPU_CHAR*" )
stub.stubFunction( ("int", "0"), "App_TCPIP_Init" )
stub.stubFunction( ("CPU_BOOLEAN", "DEF_TRUE"), "App_SerialInit" )
stub.stubFunction( ("void",), "BSP_ADC_Init" )
stub.stubFunction( ("CPU_INT32U", "0"), "BSP_CPU_ClkFreq" )
stub.stubFunction( ("void",), "BSP_HwAddr_Get", "CPU_CHAR*" )
stub.addLine( "size_t safeStrlen( const char *pStr, const size_t MaxLen )" )
stub.addLine( "{" )
stub.addLine( "    if ( pStr != NULL ) {" )
stub.addLine( "        return strnlen( pStr, MaxLen );" )
stub.addLine( "    } else {" )
stub.addLine( "        return 0;" )
stub.addLine( "    }" )
stub.addLine( "}" )
stub.newline()
stub.stubFunction( ("BSP_BctErr_t", "BCT_ERR_NONE"), "BCT_parseHeader", "BCT_Header_t *" )
stub.stubFunction( ("CPUTemperatureErr_t", "CPU_TEMPERATURE_ERR_NONE"), "BSP_ReadSingleTemperatureChAdc_K", "float *const" )
stub.stubFunction( ("uint32_t", 100), "timDrvGetResolution_NSEC", "bspClock_t" )
stub.stubFunction( ("uint32_t", 0), "timDrvGetTime_TICKS", "bspClock_t" )

stub.stubFunction( ("void",), "mpu6000_setDataReadyCallback", "mpu6000_callback_t" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "mpu6000_init", "SpiDrvDeviceCfg_t*" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "mpu6000_getData", "Mpu6000Data_t*", "int16_t*", "Mpu6000Data_t*" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "spiDrvPeriphInit", "SpiDrvPeriphCfg_t*" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "bspSpiDeviceInit", "SpiDev_t" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "spiDrvCsEnable", "SpiDrvDeviceCfg_t *" )
stub.stubFunction( ("void",), "spiDrvCsDisable", "SpiDrvDeviceCfg_t *" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "spiDrvPollSend8", "SpiDrvDeviceCfg_t *", "uint8_t" )
stub.stubFunction( ("SpiDrvErr_t", "SPI_DRV_ERR_NONE"), "spiDrvPollRead8", "SpiDrvDeviceCfg_t *", "uint8_t *" )
stub.stubFunction( ("float", "0.0F"), "mpu6000_convertTemperature_C", "int16_t" )

stub.stubFunction( ("i2cStatus_t", "I2C_SUCCESS"), "i2c_configure", "I2C_TypeDef *" )
stub.stubFunction( ("i2cStatus_t", "I2C_SUCCESS"), "i2c_selectSlave", "I2C_TypeDef *", "uint8_t" )
stub.stubFunction( ("i2cStatus_t", "I2C_SUCCESS"), "i2c_deselectSlave", "I2C_TypeDef *" )
stub.stubFunction( ("i2cStatus_t", "I2C_SUCCESS"), "i2c_txFrame", "I2C_TypeDef *", "const uint8_t *", "uint16_t", "const uint32_t" )
stub.stubFunction( ("i2cStatus_t", "I2C_SUCCESS"), "i2c_rxFrame", "I2C_TypeDef *", "uint8_t *", "uint16_t", "const uint32_t" )
stub.stubFunction( ("i2cStatus_t", "I2C_SUCCESS"), "i2c_setSpeed", "I2C_TypeDef *", "uint32_t" )


stub.stubFunction( ("void", ""), "BSP_SingleTemperatureChAdc_Init" )
stub.stubFunction( ("void", ""), "commonDrvTurnPinOn", "const SCommonDrvPin_t*" )
stub.stubFunction( ("void", ""), "commonDrvTurnPinOff", "const SCommonDrvPin_t*" )
stub.stubFunction( ("bool", "1"), "commonDrvReadPin", "const SCommonDrvPin_t*" )
stub.stubFunction( ("BSP_BctErr_t", "BCT_ERR_NONE"), "BSP_initGpio", "const char * const", "SCommonDrvPin_t*" )
stub.stubFunction( ("BSP_BctErr_t", "BCT_ERR_NONE"), "BSP_initI2c", "const char * const", "BCT_I2cPins_t *" )
stub.stubFunction( ("BSP_BctErr_t", "BCT_ERR_NONE"), "BSP_initUart", "const char * const", "BCT_UartPins_t *" )

stub.stubFunction( ("BSP_BctErr_t", "BCT_ERR_NONE"), "BCT_parseSpi", "const char * const", "BCT_SpiPins_t *" )
stub.stubFunction( ("BSP_BctErr_t", "BCT_ERR_NONE"), "BSP_initExti", "const char * const", "SCommonDrvPin_t *", "BSP_FNCT_ISR" )

stub.stubFunction( ("CPU_INT08U*", "NULL"), "App_SerialGetHilsimData", "CPU_INT08U" )

stub.addLine( "SERIAL_DEV_CFG *BSP_UART_COM1 = NULL;" )
stub.addLine( "char g_BCT_ErrLog[128];" )	

stub.stubFunction( ("uint16_t", "0U"), "crc16_modbus", "uint16_t", "const uint8_t *", "uint32_t" );
