import sys
from genStubs import *

stub = Stubs( "airmail", sys.argv[1], sys.argv[2] )

### Include headers
stub.include( "airmail/airmail.h" )
stub.include( "airmail/CAirmailObjSet.h" )
stub.include( "airmail/CDeviceManagerApi.h" )
stub.include( "airmail/CForwardingMsg.h" )
stub.include( "airmail/CNetCan.h" )
stub.include( "airmail/CNetCanAddress.h" )
stub.include( "airmail/CNetIfc.h" )
stub.include( "airmail/CNetUdp.h" )
stub.include( "airmail/CNetTx.h" )
stub.include( "airmail/CNodeInfo.h" )
stub.include( "airmail/CService.h" )
stub.newline()


### Used Namespaces
stub.useNamespace( "airware" )
stub.useNamespace( "airware::airmail" )
stub.useNamespace( "airware::airmail::internal" )
stub.useNamespace( "airware::airmail::internal::canaddr" )

stub.useNamespace( "airware::uios" )
stub.newline()


### Constructors/Destructors
# CEventInfo
stub.stubConstructor( "CEventInfo", "kind_t Kind, signatureId_t SignatureId, providerId_t ProviderId" )
stub.stubConstructor( "CEventInfo", "kind_t Kind, uniqueId_t Id" )
stub.stubConstructor( "CEventInfo", "const CEventInfo &copy, localSrc_t local" )
stub.stubConstructor( "CEventInfo", "uniqueId_t Id" )
stub.stubConstructor( "CEventInfo", "" )

# CNodeInfo
stub.stubConstructor( "CNodeInfo", "const char *, vendorId_t, productId_t, uint8_t, uint8_t, uint8_t, uniqueId_t" )

# CTopicHandler
stub.stubConstructor( "CTopicHandler", "" )
stub.stubDestructor( "CTopicHandler" )

# CBaseSocket
stub.stubConstructor( "CBaseSocket", "ISocket::name_t Name" )
stub.stubConstructor( "CBaseSocket", "ISocket::name_t Name, priority_t Priority" )

# CBaseService
stub.stubConstructor( "CBaseService", "const char *Name", "CBaseSocket( Name )" )

# CServiceHandler
stub.stubConstructor( "CServiceHandler", "" )
stub.stubDestructor( "CServiceHandler" )

### Member Functions
# CEventInfo
stub.stubConstFunction( ("signatureId_t", "0"), "CEventInfo::getSignatureId" )
stub.stubFunction( ("void",), "CEventInfo::setSignatureId", "signatureId_t" )
stub.stubFunction( ("void",), "CEventInfo::setProviderId", "providerId_t" )
stub.stubConstFunction( ("uniqueId_t","0"), "CEventInfo::getUniqueId" )
stub.stubConstFunction( ("providerId_t","0"), "CEventInfo::getProviderId" )

# CTopicHandler
stub.addLine( "static CTopicHandler s_dummyTopicHandler;" )
stub.stubConstFunction( ("const ITopicHandler&","s_dummyTopicHandler"), "CTopicHandler::getHandler" )
stub.stubConstFunction( ("void",), "CTopicHandler::handle", "const IMessage &", "const CEventInfo &" )
stub.stubConstFunction( ("bool","true"), "CTopicHandler::copy", "void *", "size_t" )

# CBaseSocket
stub.stubConstFunction( ("ISocket::name_t","\"no name\""), "CBaseSocket::getName" )
stub.stubConstFunction( ("ISocket::idHash_t","0"), "CBaseSocket::getIdHash" )
stub.stubConstFunction( ("ISocket::assignedId_t","CEventInfo()"), "CBaseSocket::getAssignedId" )
stub.stubConstFunction( ("priority_t","PRIORITY_LOW"), "CBaseSocket::getPriority" )
stub.stubFunction( ("void",), "CBaseSocket::assignUniqueId", "uniqueId_t" )

# CBaseService
stub.stubFunction( ("bool","true"), "CBaseService::sHasArgument" )
stub.stubFunction( ("bool","true"), "CBaseService::sHasReturn" )
stub.stubConstFunction( ("bool","true"), "CBaseService::hasArgument" )
stub.stubConstFunction( ("bool","true"), "CBaseService::hasReturn" )
stub.stubFunction( ("void",), "CBaseService::resetId" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "CBaseService::unregisterCaller" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "CBaseService::unregisterHandler" )
stub.stubOverload( ("status_t","AIRMAIL_OK"), "CBaseService::unregisterHandler", "CBaseService_unregisterHandler_threadId_t", "uios::threadId_t" )

#CDeviceManagerApi
stub.addLine( "CDeviceManagerApi *CDeviceManagerApi::get()      " )
stub.addLine( "{                          " )
stub.addLine( "    static CDeviceManagerApi s_CDeviceManagerApi;" )
stub.addLine( "    return &s_CDeviceManagerApi;       " )
stub.addLine( "}                          " )
stub.stubConstructor( "CDeviceManagerApi", "" )
stub.stubFunction( ("nodeId_t","0"), "CDeviceManagerApi::getNodeId" )

# CMemPool
stub.stubFunction( ("bool","true"), "CMemPool::instantiate" )
stub.stubFunction( ("bool","true"), "CMemPool::initialize", "void *", "const uint32_t", "const uint32_t", "const uint32_t", "const uint8_t", "const char *" )
stub.stubFunction( ("void",""), "CMemPool::free", "void*" )
stub.stubFunction( ("void*","NULL"), "CMemPool::alloc" )
stub.stubConstFunction( ("uint32_t","0"), "CMemPool::freeBlocks" )
stub.stubConstFunction( ("uint32_t","0"), "CMemPool::getLowWaterMark" )
stub.stubConstFunction( ("uint32_t","0"), "CMemPool::blockSize" )
stub.stubConstFunction( ("uint32_t","0"), "CMemPool::blocks" )

#CDeviceManagerBase
stub.stubConstructor( "CDeviceManagerBase", "",
                        "m_registerAsProvider( \"\" )",
                        "m_registerAsUserOf( \"\" )",
                        "m_getProvidersOf( \"\" )",
                        "m_getDefaultProviderFor( \"\" )",
                        "m_setDefaultProviderFor( \"\" )",
                        "m_ping( \"\" )",
                        "m_unregisterAsProvider( \"\" )",
                        "m_requestNodeIdOffer( \"\" )",
                        "m_requestNodeId( \"\" )",
                        "m_requestNodeInfo( \"\" )",
                        "m_requestAllNodeIds( \"\" )",
                        "m_logAllNodeIds( \"\" )" )

#CNodeThreadListHead
stub.stubConstructor( "CNodeThreadListHead", "" )

# CService<void,void>
stub.addLine( "const ISocket::socketFuns CService<void,void>::s_m_socketFuns;" )

#CNetCan
stub.stubConstructor( "CNetCan", "const char *, uint8_t",
    "CNetIfc( &m_netTx, &m_netRx )",
    "m_netRx( \"\", 0, this )",
    "m_netTx( \"\", 0, this )",
    "m_netCanAddress( 0 )" )
stub.stubDestructor( "CNetCan" )
stub.stubFunction( ("CThreadWorker*","NULL"), "CNetCan::getRxThread" )
stub.stubFunction( ("CThreadWorker*","NULL"), "CNetCan::getTxThread" )
stub.stubFunction( ("bool","true"), "CNetCan::initIfc" )
stub.stubFunction( ("uint16_t","0"), "CNetCan::checkEventSeq", "uint16_t*","uint32_t","uint16_t" )

#CNetUdp
stub.stubConstructor( "CNetUdp", "const char *, const char *",
    "CNetIfc( &m_netTx, &m_netRx )",
    "m_netRx( \"\", \"\", this, 0 )",
    "m_netTx( \"\", \"\", this )" )
stub.stubDestructor( "CNetUdp" )
stub.stubFunction( ("CThreadWorker*","NULL"), "CNetUdp::getRxThread" )
stub.stubFunction( ("CThreadWorker*","NULL"), "CNetUdp::getTxThread" )
stub.stubFunction( ("bool","true"), "CNetUdp::registerSessionMemory", "CNetRxUdp::udpSessionMemory_t *" )

#CNetIfc
stub.stubConstructor( "CNetIfc", "CNetTx *, CNetRx *",
    "m_txer( NULL )",
    "m_rxer( NULL )" )
stub.stubDestructor( "CNetIfc" )
stub.stubFunction( ("CNetTx*","NULL"), "CNetIfc::getTxer" )
stub.stubFunction( ("uint16_t","0"), "CNetIfc::checkEventSeq", "uint16_t*","uint32_t","uint16_t" )

#CNetTx
stub.stubConstructor( "CNetTx", "const char *, const char *, CEventInfo::localSrc_t, CNetIfc *ifc",
      "m_announcer( \"\" )",
      "m_msgDel( CTopicDelegate<IMessage>::delegate_t::from_method < CNetTx, &CNetTx::sendMsg > ( this ) )",
      "m_eventDel( CTopicDelegate<IMessage>::delegate_t::from_method < CNetTx, &CNetTx::sendEvent > ( this ) )",
      "m_forwardingTopic( \"\" )",
      "m_subTo( \"\" )",
      "m_provideNetSvc( \"\" )",
      "m_provNetDelegate( CServiceDelegate<CAnnounceMsg, void>::delegate_t::from_method < CNetTx, &CNetTx::provNetHandler > ( this ) )",
      "m_nakTopic( \"\" )" )
stub.stubFunction( ("ipAddress_t","0"), "CNetTx::getInterfaceAddress" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CNetTx::onStart" )
stub.stubFunction( ("void",), "CNetTx::onLoop" )
stub.stubFunction( ("void",), "CNetTx::handleNak", "CNakMsg const &", "CEventInfo const &" )
stub.stubFunction( ("void",), "CNetTx::sendMsg", "IMessage const &", "CEventInfo const &" )
stub.stubFunction( ("void",), "CNetTx::sendEvent", "IMessage const &", "CEventInfo const &" )
stub.stubFunction( ("int32_t","0"), "CNetTx::provNetHandler", "CAnnounceMsg const &" )
stub.stubFunction( ("void",), "CNetTx::txReliable", "uint8_t const *", "uint32_t", "bool" )
stub.stubFunction( ("void",), "CNetTx::txUnreliable", "uint8_t const *", "uint32_t", "bool" )


#CNetRx
stub.stubConstructor( "CNetRx", "const char *, CEventInfo::localSrc_t, CNetIfc *",
    "m_nakTopic( \"\" )",
    "m_subTo( \"\" )",
    "m_provNetSvc( \"\" )",
    "m_ifc( NULL )",
    "m_unregs( \"\" )",
    "m_urDel( CTopicDelegate<CAnnounceMsg>::delegate_t::from_method < CNetRx,&CNetRx::handleUnreg > ( this ) )",
    "m_forwardingTopic( \"\" )" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CNetRx::onStart" )
stub.stubFunction( ("void",), "CNetRx::onLoop" )
stub.stubFunction( ("void",), "CNetRx::handleUnreg", "CAnnounceMsg const &", "CEventInfo const &" )

#CMsgCache
stub.stubConstructor( "CMsgCache", "void" )

#CNetCanAddress
stub.stubConstructor( "CNetCanAddress", "const char *" )
stub.stubDestructor( "CNetCanAddress" )

#CNetCanAddrMgr
stub.stubConstructor( "CNetCanAddrMgr", "", "m_addrMgr( 1U )" )
stub.stubDestructor( "CNetCanAddrMgr" )

#CNetRxCan
stub.stubConstructor( "CNetRxCan", "const char *, CEventInfo::localSrc_t, CNetCan *","CNetRx( \"\", 0, NULL )" )
stub.stubFunction( ("ssize_t","0"), "CNetRxCan::receiveFrame", "uint16_t", "uint8_t*", "uint32_t","uint32_t*","uint16_t*" )

#CNetRxUdp
stub.stubConstructor( "CNetRxUdp", "const char *, const char *, CNetIfc *, uint32_t","CNetRx( \"\", 0, NULL )" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CNetRxUdp::onStart" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CNetRxUdp::onStop" )
stub.stubFunction( ("ssize_t","0"), "CNetRxUdp::receiveFrame", "uint16_t", "uint8_t*", "uint32_t","uint32_t*","uint16_t*" )
stub.stubFunction( ("void",""), "CNetRxUdp::sendNak", "uint16_t", "uint32_t", "uint16_t" )
stub.stubFunction( ("int32_t","0"), "CNetRxUdp::rxReliable", "uint8_t*", "uint16_t" )

#CNetTxCan
stub.stubConstructor( "CNetTxCan", "const char *, CEventInfo::localSrc_t, CNetCan *","CNetTx( \"\", \"\", 0, NULL )" )
stub.stubFunction( ("void",), "CNetTxCan::txReliable", "uint8_t const *", "uint32_t", "bool" )
stub.stubFunction( ("void",), "CNetTxCan::txUnreliable", "uint8_t const *", "uint32_t", "bool" )

#CNetTxUdp
stub.stubConstructor( "CNetTxUdp", "const char *, const char *, CNetIfc *","CNetTx( \"\", \"\", 0, NULL )" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CNetTxUdp::onStart" )
stub.stubFunction( ("void",), "CNetTxUdp::onLoop" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CNetTxUdp::onStop" )
stub.stubFunction( ("void",), "CNetTxUdp::txReliable", "uint8_t const *", "uint32_t", "bool" )
stub.stubFunction( ("void",), "CNetTxUdp::txUnreliable", "uint8_t const *", "uint32_t", "bool" )

#CForwardingMsg
stub.stubConstructor( "CForwardingMsg", "void" )
stub.stubConstFunction( ("int16_t","0"), "CForwardingMsg::getSerializedSize")
stub.stubConstFunction( ("int16_t","0"), "CForwardingMsg::getMaxSerializedSize")
stub.stubConstFunction( ("int16_t","0"), "CForwardingMsg::serialize", "uint8_t *", "size_t")
stub.stubFunction( ("int16_t","0"), "CForwardingMsg::deserialize", "const uint8_t *", "size_t")
stub.stubConstFunction( ("IMessage*","NULL"), "CForwardingMsg::copy", "void*")
stub.stubFunction( ("void",""), "CForwardingMsg::copyFrom", "const IMessage &")
stub.stubConstFunction( ("size_t","0"), "CForwardingMsg::sizeOf" )

### Global Functions
stub.stubFunction( ("void",), "airmail::internal::checkLock" )
stub.stubFunction( ("void *","NULL"), "airmail::internal::poolAlloc", "uint16_t" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::subscribeToPeriodic", "ISocket *", "const CTopicHandler &", "ISocket::rate_t", "providerId_t" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::subscribe", "ISocket *", "const CTopicHandler &", "IEventQueue *", "providerId_t" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::unsubscribe", "ISocket *", "unsigned int" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::unRegPublisher", "ISocket *", "unsigned int" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::wait", "uint16_t" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::registerServiceHandler", "ISocket *", "IServiceHandler *", "bool", "CNetIfc *" )
stub.stubOverload( ("status_t","AIRMAIL_OK"), "airmail::internal::registerServiceHandler", "airmail_internal_registerServiceHandlerOverload", "ISocket *", "CServiceHandler", "bool", "CNetIfc *" )

stub.stubFunction( ("status_t", "AIRMAIL_OK"), "airmail::initAirmail", "const CNodeInfo &" )
stub.stubFunction( ("status_t", "AIRMAIL_OK"), "airmail::addNetInterface", "size_t", "INetIfc *" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::publish", "CEventInfo const &", "IMessage const &" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::registerPeriodicPublisher", "ISocket *", "unsigned short" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::registerEventPublisher", "ISocket *" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::internal::callService", "ISocket *", "IMessage const *", "IMessage *", "int *", "unsigned short" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::CBaseService::registerAsCaller" )
stub.stubFunction( ("status_t","AIRMAIL_OK"), "airmail::setDestQueue", "uios::IMsgQueue<void *> *", "size_t" )
stub.stubFunction( ("int","1"), "airmail_aton", "const char*", "uint32_t*" )

# Singletons
stub.addLine( "CMemPoolSet    objMem( NULL, 0);" )
stub.addLine( "CAirmailObjSet objPools( objMem, NULL, NULL, NULL, NULL, NULL, NULL);" )
stub.addLine( "CMemPoolSet    msgPools( NULL, 0 );" )
stub.newline()

stub.stubFunction( ("uint32_t","70"), "airware::airmail::countTopicTable" )
stub.stubFunction( ("uint32_t","100"), "airware::airmail::maxTopicTable" )
stub.stubFunction( ("uint32_t","70"), "airware::airmail::countTopicHandler" )
stub.stubFunction( ("uint32_t","100"), "airware::airmail::maxTopicHandler" )
stub.stubFunction( ("uint32_t","70"), "airware::airmail::countTopicSignature" )
stub.stubFunction( ("uint32_t","100"), "airware::airmail::maxTopicSignature" )
stub.stubFunction( ("uint32_t","70"), "airware::airmail::countServiceTable" )
stub.stubFunction( ("uint32_t","100"), "airware::airmail::maxServiceTable" )
stub.stubFunction( ("uint32_t","70"), "airware::airmail::countDestTable" )
stub.stubFunction( ("uint32_t","100"), "airware::airmail::maxDestTable" )
stub.stubFunction( ("uint32_t","70"), "airware::airmail::countDMSignature" )
stub.stubFunction( ("uint32_t","100"), "airware::airmail::maxDMSignature" )
stub.stubFunction( ("uint32_t","70"), "airware::airmail::countDMProvider" )
stub.stubFunction( ("uint32_t","100"), "airware::airmail::maxDMProvider" )
stub.stubFunction( ("uint32_t","70"), "airware::airmail::countNodeId" )
stub.stubFunction( ("uint32_t","100"), "airware::airmail::maxNodeId" )

stub.stubFunction( ("const CAirmailObjSet *","&objPools"), "airware::airmail::getAirmailMem" )
stub.stubFunction( ("const CMemPoolSet *","&msgPools"), "airware::airmail::getMemPools" )

stub.stubConstFunction( ("bool","true"), "CAirmailObjSet::hasDeviceManager" )
stub.stubConstFunction( ("const CMemPoolSet&","objMem"), "CAirmailObjSet::getMemPools" )
stub.stubConstFunction( ("const CMemPool *","NULL"), "CMemPoolSet::getNextPool", "bool" )