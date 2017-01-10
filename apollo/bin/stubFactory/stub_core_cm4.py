import sys
from genStubs import *

stub = Stubs( "core_cm4", sys.argv[1], sys.argv[2] )

stub.externC()
stub.newline()

stub.stubFunction( ("void",), "__disable_irq" )
stub.stubFunction( ("void",), "NVIC_SystemReset" )
