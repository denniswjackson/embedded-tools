import sys
from genStubs import *

stub = Stubs( "jtagFuse", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "CJtagFuse.h" )
stub.newline()

### Used Namespaces
stub.useNamespace( "airware::pkidUUT" )
stub.newline()

stub.stubConstructor( "CJtagFuse", "" )
stub.stubDestructor( "CJtagFuse" )

# CMoneta class member functions
stub.stubFunction( ( "bool", "true" ), "CJtagFuse::setJtagProtectionLevel", "CJtagFuse::jtagProtectionLevel" )
stub.stubFunction( ( "CJtagFuse::jtagProtectionLevel", "CJtagFuse::LEVEL_NONE" ), "CJtagFuse::getJtagProtectionLevel" )

