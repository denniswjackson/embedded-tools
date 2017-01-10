import sys
from genStubs import *

stub = Stubs( "logger", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "logger/CLogServices.h" )
stub.include( "logger/CLogApi.h" )
stub.newline()

### Used Namespaces
stub.useNamespace( "airware::airmail" )
stub.useNamespace( "airware::logger" )
stub.useNamespace( "airware::uios" )
stub.newline()

## CLogServices
stub.stubConstructor( "CLogServices", "uint32_t",
                      "m_managementService( 0 )", )
stub.stubDestructor( "CLogServices" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CLogServices::onStart" )
stub.stubFunction( ("void",), "CLogServices::onLoop" )

## CLogManagementService
stub.stubConstructor( "CLogManagementService", "uint32_t",
                      "m_svc( \"\" )", )
stub.stubDestructor( "CLogManagementService" )

## Log Message
stub.stubFunction( ("void",""), "airware::logger::awLogMessage", "loggerId_t", "IMessage const &" )
stub.stubOverload( ("void",""), "airware::logger::awLogMessage", "loggerId_t", "loggerId_t", "sourceId_t", "IMessage const &" )