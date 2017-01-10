import sys
from genStubs import *

stub = Stubs( "admBsp", sys.argv[1], sys.argv[2] )

stub.include("radio/radioBaseBsp.h")
stub.newline()

stub.stubFunction( ("void",), "BSP_Microhard_GetLEDStates", "microhard_led_states_t*" )
