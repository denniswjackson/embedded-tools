import sys
from genStubs import *

stub = Stubs( "egbBsp", sys.argv[1], sys.argv[2] )

stub.include("radio/radioBaseBsp.h")
stub.newline()

stub.stubFunction( ("void",), "BSP_Led1Red" )
stub.stubFunction( ("void",), "BSP_Led1Grn" )
stub.stubFunction( ("void",), "BSP_Led1Off" )
stub.stubFunction( ("void",), "BSP_Led2Red" )
stub.stubFunction( ("void",), "BSP_Led2Grn" )
stub.stubFunction( ("void",), "BSP_Led2Off" )
