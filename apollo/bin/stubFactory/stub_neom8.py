import sys
from genStubs import *

stub = Stubs( "neom8", sys.argv[1], sys.argv[2] )

stub.include("NeoM8.h")
stub.newline()

stub.stubConstructor( "NeoM8", "const char * const PUartName", "m_config( )",
                                                               "m_uart( PUartName )",
                                                               "m_driverState( DRIVERSTATE_POWERON )",
                                                               "m_ubxParser( )",
                                                               "m_navPvtHandler( NULL )",
                                                               "m_navSatHandler( NULL )",
                                                               "m_navStatusHandler( NULL )",
                                                               "m_expectedAckAck( )",
                                                               "m_expectedAckAckReceived( false )",
                                                               "m_expectedCfgPrt( )",
                                                               "m_expectedCfgPrtReceived( false )" )
stub.stubFunction( ("NeoM8::Error_t","NeoM8::ERROR_NONE"), "NeoM8::init", "const NeoM8::SConfig * const" )
stub.stubFunction( ("void",), "NeoM8::setNavPvtHandler", "const NeoM8::NavPvtHandler_t" )
stub.stubFunction( ("void",), "NeoM8::setNavSatHandler", "const NeoM8::NavSatHandler_t" )
stub.stubFunction( ("void",), "NeoM8::setNavStatusHandler", "const NeoM8::NavStatusHandler_t" )
stub.stubFunction( ("void",), "NeoM8::hardReset" )
stub.stubFunction( ("NeoM8::Error_t","NeoM8::ERROR_NONE"), "NeoM8::softReset", "const Ubx::CfgRst::ResetMode_t", "const Ubx::CfgRst::NavBbrMask_t" )
stub.stubFunction( ("NeoM8::Error_t","NeoM8::ERROR_NONE"), "NeoM8::process", "const uint32_t" )