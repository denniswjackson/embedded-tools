import sys
from genStubs import *

stub = Stubs( "ubx", sys.argv[1], sys.argv[2] )

stub.include("ubx/UbxCommon.h")
stub.include("ubx/AckAck.h")
stub.include("ubx/AckNack.h")
stub.include("ubx/CfgGnss.h")
stub.include("ubx/CfgMsg.h")
stub.include("ubx/CfgNav5.h")
stub.include("ubx/CfgPrt.h")
stub.include("ubx/CfgRate.h")
stub.include("ubx/CfgRst.h")
stub.include("ubx/NavPvt.h")
stub.include("ubx/NavSat.h")
stub.include("ubx/NavStatus.h")
stub.include("ubx/UbxParser.h")
stub.newline()

stub.useNamespace( "Ubx" )
stub.newline()

stub.stubFunction( ("uint16_t","0"), "UbxCommon::checksum", "const uint8_t * const", "const uint16_t" )
stub.stubFunction( ("bool","true"),  "UbxCommon::isClassIdValid", "const UbxCommon::ClassId_t" )
stub.stubFunction( ("bool","true"),  "UbxCommon::isMessageIdValid", "const UbxCommon::MessageId_t" )

stub.stubConstructor( "AckAck", "", "m_clsID( 0 )",
                                    "m_msgID( 0 )" )
stub.stubConstFunction( ("uint16_t","AckAck::MAX_PAYLOAD_LENGTH"), "AckAck::payloadLength" )
stub.stubConstFunction( ("uint16_t","AckAck::MAX_MESSAGE_LENGTH"), "AckAck::messageLength" )
stub.stubConstFunction( ("bool","true"), "AckAck::compare", "const AckAck * const" )
stub.stubFunction( ("UbxCommon::Error_t","UbxCommon::ERROR_NONE"), "AckAck::deserialize", "const uint8_t * const", "const uint16_t" )

stub.stubConstructor( "AckNack", "", "m_clsID( 0 )",
                                     "m_msgID( 0 )" )
stub.stubConstFunction( ("uint16_t","AckNack::MAX_PAYLOAD_LENGTH"), "AckNack::payloadLength" )
stub.stubConstFunction( ("uint16_t","AckNack::MAX_MESSAGE_LENGTH"), "AckNack::messageLength" )
stub.stubFunction( ("UbxCommon::Error_t","UbxCommon::ERROR_NONE"), "AckNack::deserialize", "const uint8_t * const", "const uint16_t" )

stub.stubConstructor( "CfgGnss", "", "m_msgVer( 0 )",
                                     "m_numTrkChHw( 0 )",
                                     "m_numTrkChUse( MAX_NUMTRKCHUSE )",
                                     "m_numConfigBlocks( MAX_CFG_BLOCKS )" )
stub.stubConstFunction( ("bool","true"), "CfgGnss::isValid" )
stub.stubConstFunction( ("uint16_t","CfgGnss::MAX_PAYLOAD_LENGTH"), "CfgGnss::payloadLength" )
stub.stubConstFunction( ("uint16_t","CfgGnss::MAX_MESSAGE_LENGTH"), "CfgGnss::messageLength" )
stub.stubConstFunction( ("uint16_t","CfgGnss::MAX_MESSAGE_LENGTH"), "CfgGnss::serialize", "uint8_t * const", "const uint16_t" )

stub.stubConstructor( "CfgMsg", "", "m_msgClass( 0 )",
                                    "m_msgID( 0 )" )
stub.stubConstFunction( ("uint16_t","CfgMsg::MAX_PAYLOAD_LENGTH"), "CfgMsg::payloadLength" )
stub.stubConstFunction( ("uint16_t","CfgMsg::MAX_MESSAGE_LENGTH"), "CfgMsg::messageLength" )
stub.stubConstFunction( ("uint16_t","CfgMsg::MAX_MESSAGE_LENGTH"), "CfgMsg::serialize", "uint8_t * const", "const uint16_t" )

stub.stubConstructor( "CfgNav5", "", "m_mask()",
                                     "m_dynModel( DYNMODEL_PORTABLE )",
                                     "m_fixMode( FIXMODE_AUTO )",
                                     "m_fixedAlt( 0 )",
                                     "m_fixedAltVar( 10000U )",
                                     "m_minElev( 5U )",
                                     "m_drLimit( 0 )",
                                     "m_pDop( 250U )",
                                     "m_tDop( 250U )",
                                     "m_pAcc( 100U )",
                                     "m_tAcc( 300U )",
                                     "m_staticHoldThresh( 0 )",
                                     "m_dgpsTimeOut( 60U )",
                                     "m_cnoThreshNumSVs( 0 )",
                                     "m_cnoThresh( 0 )",
                                     "m_staticHoldMaxDist( 200U )",
                                     "m_utcStandard( UTCSTANDARD_AUTO )" )
stub.stubConstFunction( ("uint16_t","CfgNav5::MAX_PAYLOAD_LENGTH"), "CfgNav5::payloadLength" )
stub.stubConstFunction( ("uint16_t","CfgNav5::MAX_MESSAGE_LENGTH"), "CfgNav5::messageLength" )
stub.stubConstFunction( ("uint16_t","CfgNav5::MAX_MESSAGE_LENGTH"), "CfgNav5::serialize", "uint8_t * const", "const uint16_t" )

stub.stubConstructor( "CfgPrt", "", "m_portID( UbxCommon::PORTID_UART1 )",
                                    "m_txReady( )",
                                    "m_mode( )",
                                    "m_baudRate( 0 )",
                                    "m_inProtoMask( )",
                                    "m_outProtoMask( )",
                                    "m_flags( )",
                                    "m_isPolling( false )" )
stub.stubConstFunction( ("uint16_t","CfgPrt::MAX_PAYLOAD_LENGTH"), "CfgPrt::payloadLength" )
stub.stubConstFunction( ("uint16_t","CfgPrt::MAX_MESSAGE_LENGTH"), "CfgPrt::messageLength" )
stub.stubFunction( ("void",), "CfgPrt::poll", "const bool" )
stub.stubConstFunction( ("bool","true"), "CfgPrt::compare", "const CfgPrt * const" )
stub.stubFunction( ("UbxCommon::Error_t","UbxCommon::ERROR_NONE"), "CfgPrt::deserialize", "const uint8_t * const", "const uint16_t" )
stub.stubConstFunction( ("uint16_t","CfgPrt::MAX_MESSAGE_LENGTH"), "CfgPrt::serialize", "uint8_t * const", "const uint16_t" )

stub.stubConstructor( "CfgRate", "", "m_measRate( 1000 )",
                                     "m_navRate( 1 )",
                                     "m_timeRef( TIMEREF_GPS )" )
stub.stubConstFunction( ("uint16_t","CfgRate::MAX_PAYLOAD_LENGTH"), "CfgRate::payloadLength" )
stub.stubConstFunction( ("uint16_t","CfgRate::MAX_MESSAGE_LENGTH"), "CfgRate::messageLength" )
stub.stubConstFunction( ("uint16_t","CfgRate::MAX_MESSAGE_LENGTH"), "CfgRate::serialize", "uint8_t * const", "const uint16_t" )

stub.stubConstructor( "CfgRst", "", "m_navBbrMask( NAVBBRMASK_HOT )",
                                    "m_resetMode( RESETMODE_SOFTWARE_GNSS )" )
stub.stubConstFunction( ("uint16_t","CfgRst::MAX_PAYLOAD_LENGTH"), "CfgRst::payloadLength" )
stub.stubConstFunction( ("uint16_t","CfgRst::MAX_MESSAGE_LENGTH"), "CfgRst::messageLength" )
stub.stubConstFunction( ("uint16_t","CfgRst::MAX_MESSAGE_LENGTH"), "CfgRst::serialize", "uint8_t * const", "const uint16_t" )

stub.stubConstructor( "NavPvt", "", "m_iTOW( 0 )",
                                    "m_year( 0 )",
                                    "m_month( 0 )",
                                    "m_day( 0 )",
                                    "m_hour( 0 )",
                                    "m_min( 0 )",
                                    "m_sec( 0 )",
                                    "m_valid( )",
                                    "m_tAcc( 0 )",
                                    "m_nano( 0 )",
                                    "m_fixType( FIXTYPE_NO_FIX )",
                                    "m_flags( )",
                                    "m_numSV( 0 )",
                                    "m_lon( 0 )",
                                    "m_lat( 0 )",
                                    "m_height( 0 )",
                                    "m_hMSL( 0 )",
                                    "m_hAcc( 0 )",
                                    "m_vAcc( 0 )",
                                    "m_velN( 0 )",
                                    "m_velE( 0 )",
                                    "m_velD( 0 )",
                                    "m_gSpeed( 0 )",
                                    "m_headMot( 0 )",
                                    "m_sAcc( 0 )",
                                    "m_headAcc( 0 )",
                                    "m_pDOP( 0 )",
                                    "m_headVeh( 0 )" )
stub.stubConstFunction( ("uint16_t","NavPvt::MAX_PAYLOAD_LENGTH"), "NavPvt::payloadLength" )
stub.stubConstFunction( ("uint16_t","NavPvt::MAX_MESSAGE_LENGTH"), "NavPvt::messageLength" )
stub.stubFunction( ("UbxCommon::Error_t","UbxCommon::ERROR_NONE"), "NavPvt::deserialize", "const uint8_t * const", "const uint16_t" )

stub.stubConstructor( "NavSat", "", "m_iTOW( 0 )",
                                    "m_version( 0 )",
                                    "m_numSvs( 0 )" )
stub.stubConstFunction( ("bool","true"), "NavSat::isValid" )
stub.stubConstFunction( ("uint16_t","NavSat::MAX_PAYLOAD_LENGTH"), "NavSat::payloadLength" )
stub.stubConstFunction( ("uint16_t","NavSat::MAX_MESSAGE_LENGTH"), "NavSat::messageLength" )
stub.stubFunction( ("UbxCommon::Error_t","UbxCommon::ERROR_NONE"), "NavSat::deserialize", "const uint8_t * const", "const uint16_t" )

stub.stubConstructor( "NavStatus", "", "m_iTOW( 0 )",
                                       "m_gpsFix( GPSFIX_NO_FIX )",
                                       "m_flags( )",
                                       "m_fixStat( )",
                                       "m_flags2( )",
                                       "m_ttff( 0 )",
                                       "m_msss( 0 )" )
stub.stubConstFunction( ("uint16_t","NavStatus::MAX_PAYLOAD_LENGTH"), "NavStatus::payloadLength" )
stub.stubConstFunction( ("uint16_t","NavStatus::MAX_MESSAGE_LENGTH"), "NavStatus::messageLength" )
stub.stubFunction( ("UbxCommon::Error_t","UbxCommon::ERROR_NONE"), "NavStatus::deserialize", "const uint8_t * const", "const uint16_t" )

stub.stubConstructor( "UbxParser", "", "m_writePointer( &m_internalBuffer[ 0 ] )",
                                       "m_remainingPayload( 0 )",
                                       "m_state( PARSERSTATE_SYNC1 )",
                                       "m_ackAck( )",
                                       "m_ackNack( )",
                                       "m_cfgPrt( )",
                                       "m_navPvt( )",
                                       "m_navSat( )",
                                       "m_navStatus( )" )
stub.stubFunction( ("uint32_t","0"), "UbxParser::parse", "UbxCommon::ClassId_t * const", "UbxCommon::MessageId_t * const", "UbxCommon::Error_t * const", "const uint8_t * const", "const uint32_t" )
stub.stubConstFunction( ("const AckAck &","AckAck()"), "UbxParser::lastAckAck" )
stub.stubConstFunction( ("const AckNack &","AckNack()"), "UbxParser::lastAckNack" )
stub.stubConstFunction( ("const CfgPrt &","CfgPrt()"), "UbxParser::lastCfgPrt" )
stub.stubConstFunction( ("const NavPvt &","NavPvt()"), "UbxParser::lastNavPvt" )
stub.stubConstFunction( ("const NavSat &","NavSat()"), "UbxParser::lastNavSat" )
stub.stubConstFunction( ("const NavStatus &","NavStatus()"), "UbxParser::lastNavStatus" )
stub.stubFunction( ("void",), "UbxParser::reset" )