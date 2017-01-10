import sys
from genStubs import *

stub = Stubs( "airBoot", sys.argv[1], sys.argv[2] )

stub.include( "airBoot/airBootFlags.h" )
stub.newline()

stub.stubFunction( ("void",), "airwareExit", "int" )


stub.addLine( "static SAirBootFlags s_airBootFlags;" )

stub.stubFunction( ( "SAirBootFlags &", "s_airBootFlags" ), "getAirBootFlags" )
stub.stubFunction( ( "bool", "true" ), "SAirBootFlags::open" )
