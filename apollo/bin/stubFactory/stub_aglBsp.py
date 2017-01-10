import sys
from genStubs import *

stub = Stubs( "aglBsp", sys.argv[1], sys.argv[2] )

stub.include("agl/aglBsp.h")
stub.newline()

stub.addLine("SERIAL_DEV_CFG *LIDAR_COM_PORT = NULL;")

stub.stubFunction( ("bool","true"), "BSP_OSInit" )
stub.stubFunction( ("BSP_BctErr_t","BCT_ERR_NONE"), "BSP_Init" )

stub.stubFunction( ("void",), "BSP_DisablePWMCameraPort" )
stub.stubFunction( ("void",), "BSP_DisablePulseCameraPort" )
stub.stubFunction( ("bool","true"), "BSP_EnablePulseCameraPort", "CPU_FNCT_VOID" )
stub.stubFunction( ("bool","true"), "BSP_ReadCameraInput" )
stub.stubFunction( ("bool","true"), "BSP_SetPulseCamera" )
stub.stubFunction( ("bool","true"), "BSP_ResetPulseCamera" )
stub.stubFunction( ("bool","true"), "BSP_ReadPulseCamera", "bool*" )
stub.stubFunction( ("bool","true"), "BSP_IsPort4Available" )
stub.stubFunction( ("bool","true"), "BSP_EnablePWMCameraPort", "const uint32_t", "CPU_FNCT_VOID" )
# stub.stubFunction( ("bool","true"), "BSP_ConfigurePWMOutput", "const actuatorPortNumber_t" )
# stub.stubFunction( ("bool","true"), "BSP_EnablePWM", "const actuatorPortNumber_t" )
