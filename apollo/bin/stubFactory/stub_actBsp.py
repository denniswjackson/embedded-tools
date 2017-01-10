import sys
from genStubs import *

stub = Stubs( "actBsp", sys.argv[1], sys.argv[2] )

stub.include("actuator/actBsp.h")
stub.newline()

stub.externC()

stub.stubFunction( ("bool", "true"), "BSP_EnablePWM", "const actuatorPortNumber_t" )
stub.stubFunction( ("bool", "true"), "BSP_DisablePWM", "const actuatorPortNumber_t" )
stub.stubFunction( ("void",), "BSP_SetPWMRate", "const PWMRateMsg_PWMRateType" )
stub.stubFunction( ("bool", "true"), "BSP_ConfigurePWMOutput", "const actuatorPortNumber_t" )
stub.stubFunction( ("void",), "BSP_SetPWMOutputValue", "const actuatorPortNumber_t", "const uint32_t" )
stub.stubFunction( ("actuatorPortNumber_t", "actuatorPortNumber_t_PORT_4"), "BSP_MaxOuputPort" )
stub.stubFunction( ("bool", "true"), "BSP_ReadPWMChannel", "const actuatorPortNumber_t", "uint32_t*" )
stub.stubFunction( ("bool", "true"), "BSP_GetPWMRate", "PWMRateMsg_PWMRateType*" )

# Act04p
stub.stubFunction( ("bool", "true"), "BSP_EnableSbusInput" )
stub.stubFunction( ("void", ""), "BSP_DisableSbusInput" )
stub.stubFunction( ("bool", "true"), "BSP_EnableSbusOutput" )
stub.stubFunction( ("void", ""), "BSP_DisableSbusOutput" )
stub.stubFunction( ("bool", "true"), "BSP_EnablePWMCameraPort", "const uint32_t", "CPU_FNCT_VOID" )
stub.stubFunction( ("void", ""), "BSP_DisablePWMCameraPort" )
stub.stubFunction( ("bool", "true"), "BSP_EnablePulseCameraPort", "CPU_FNCT_VOID" )
stub.stubFunction( ("void", ""), "BSP_DisablePulseCameraPort" )
stub.stubFunction( ("bool", "true"), "BSP_ReadCameraInput" )
stub.stubFunction( ("bool", "true"), "BSP_EnableI2C" )
stub.stubFunction( ("void", ""), "BSP_DisableI2C" )
stub.stubFunction( ("void", ""), "BSP_ConfigureBusPowerSource", "PowerBus_t" )
stub.stubFunction( ("bool", "true"), "BSP_SetPWMCameraOutput", "const uint32_t" )
stub.stubFunction( ("bool", "true"), "BSP_SetPulseCamera" )
stub.stubFunction( ("bool", "true"), "BSP_ResetPulseCamera" )
stub.stubFunction( ("bool", "true"), "BSP_Is5VSCBusFaulted" )
stub.stubFunction( ("bool", "true"), "BSP_ReadPulseCamera", "bool *" )
stub.stubFunction( ("bool", "true"), "BSP_IsPort1Available" )
stub.stubFunction( ("bool", "true"), "BSP_IsPort2Available" )
stub.stubFunction( ("bool", "true"), "BSP_IsPort3Available" )
stub.stubFunction( ("bool", "true"), "BSP_IsPort4Available" )
