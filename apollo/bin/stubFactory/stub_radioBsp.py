import sys
from genStubs import *

stub = Stubs( "radioBsp", sys.argv[1], sys.argv[2] )

stub.include("radio/radioBaseBsp.h")
stub.include("bsp_spi.h")
stub.newline()

stub.stubFunction( ("void", ""), "BSP_MicrohardNano_On" )
stub.stubFunction( ("void", ""), "BSP_MicrohardNanoDDL_On" )
stub.stubFunction( ("void", ""), "BSP_Microhard_Off" )

stub.stubFunction( ("void", ""), "BSP_Microhard_GetLEDStates", "microhard_led_states_t *" )

stub.stubFunction( ("bool", "true"), "BSP_AddMicrohard_ComPorts" )
stub.stubFunction( ("bool", "true"), "BSP_ResetButton_Enable", "CPU_FNCT_VOID" )
stub.stubFunction( ("void", ""), "BSP_ResetButton_Disable" )

stub.addLine( "const char *g_MICROHARD_PORT_NAME = \"COM_DUMMY\";" )
stub.addLine( "const char *g_MICROHARD_COM2_NAME = \"COM_DUMMY\";" )

stub.stubFunction( ("SpiDrvDeviceCfg_t *", "NULL"), "bspGetSpiDeviceCfg", "SpiDev_t" )

stub.externC()

stub.stubFunction( ("void", ""), "BSP_netif_set_up", "struct netif *" )
stub.stubFunction( ("void", ""), "BSP_netif_set_down", "struct netif *" )
