import sys
from genStubs import *

stub = Stubs( "scap", sys.argv[1], sys.argv[2] )


stub.include( "scap/CContingencyManager.h" )
stub.include( "scap/CMissionManager.h" )
stub.include( "scap/COperatorModule.h" )
stub.newline()

stub.useNamespace( "airware::scap" )
stub.useNamespace( "airware::uios" )
stub.newline()

# Constructors
stub.stubConstructor( "CContingencyManager", "",
                      "CManeuverSource( ControlRequest_controlRequestorType_CONTINGENCY_MANAGER ),"
                      "m_rcCommandTopic( \"airware.RcInputMsg\" ),"
                      "m_rcCommandCallback(airware::airmail::CTopicDelegate<CRcInputMsg>::delegate_t::from_method<CContingencyManager, &CContingencyManager::rcCommandHandler>( this ) ),"
                      "m_missionUploadSvc( \"airware.contingencyMissionUploadSvc\" ),"
                      "m_maneuverUploadSvc( \"airware.contingencyManeuverUploadSvc\" ),"
                      "m_maneuverDownloadSvc( \"airware.contingencyManeuverDownloadSvc\" ),"
                      "m_missionListSvc( \"airware.contingencyMissionListSvc\" ),"
                      "m_missionDownloadSvc( \"airware.contingencyMissionDownloadSvc\" ),"
                      "m_missionStatusTopic( \"airware.contingencyMissionStatus\" ),"
                      "m_contingencyEventStatusTopic( \"airware.contingencyEventStatus\" ),"
                      "m_missionUploadCallback(airware::airmail::CServiceDelegate<CMission, CMission>::delegate_t::from_method<CContingencyManager, &CContingencyManager::missionUploadHandler>( this ) ),"
                      "m_maneuverUploadCallback(airware::airmail::CServiceDelegate<CManeuver, void>::delegate_t::from_method<CContingencyManager, &CContingencyManager::maneuverUploadHandler>( this ) ),"
                      "m_maneuverDownloadCallback(airware::airmail::CServiceDelegate<CManeuver, CManeuver>::delegate_t::from_method<CContingencyManager, &CContingencyManager::maneuverDownloadHandler>( this ) ),"
                      "m_missionListCallback(airware::airmail::CServiceDelegate<void, CMissionList>::delegate_t::from_method<CContingencyManager, &CContingencyManager::missionListHandler>( this ) ),"
                      "m_missionDownloadCallback(airware::airmail::CServiceDelegate<CMission, CMission>::delegate_t::from_method<CContingencyManager, &CContingencyManager::missionDownloadHandler>( this ) )" )

stub.stubConstructor( "CMissionManager", "",
                      "CManeuverSource( ControlRequest_controlRequestorType_MISSION_MANAGER ),"
                      "m_missionControlRequestSvc( \"airware.missionControlRequestSvc\" ),"
                      "m_missionUploadSvc( \"airware.missionUploadSvc\" ),"
                      "m_missionDownloadSvc( \"airware.missionDownloadSvc\" ),"
                      "m_maneuverUploadSvc( \"airware.maneuverUploadSvc\" ),"
                      "m_maneuverDownloadSvc( \"airware.maneuverDownloadSvc\" ),"
                      "m_missionExecSvc( \"airware.missionExecSvc\" ),"
                      "m_keepAliveSvc( \"airware.gcsMissionKeepAliveSvc\" ),"
                      "m_missionListSvc( \"airware.missionListSvc\" ),"
                      "m_missionStatusTopic( \"airware.missionStatus\" ),"
                      "m_activeMissionSourceNotificationTopic( \"airware.activeMissionSourceNotification\" ),"
                      "m_missionControlRequestCallback(airware::airmail::CServiceDelegate<CControlRequest, void>::delegate_t::from_method<CMissionManager, &CMissionManager::missionControlRequestHandler>( this ) ),"
                      "m_missionUploadCallback(airware::airmail::CServiceDelegate<CMission, CMission>::delegate_t::from_method<CMissionManager, &CMissionManager::missionUploadHandler>( this ) ),"
                      "m_missionDownloadCallback(airware::airmail::CServiceDelegate<CMission, CMission>::delegate_t::from_method<CMissionManager, &CMissionManager::missionDownloadHandler>( this ) ),"
                      "m_maneuverUploadCallback(airware::airmail::CServiceDelegate<CManeuver, void>::delegate_t::from_method<CMissionManager, &CMissionManager::maneuverUploadHandler>( this ) ),"
                      "m_maneuverDownloadCallback(airware::airmail::CServiceDelegate<CManeuver, CManeuver>::delegate_t::from_method<CMissionManager, &CMissionManager::maneuverDownloadHandler>( this ) ),"
                      "m_missionExecCallback(airware::airmail::CServiceDelegate<CMissionExec, void>::delegate_t::from_method<CMissionManager, &CMissionManager::missionExecHandler>( this ) ),"
                      "m_keepAliveCallback(airware::airmail::CServiceDelegate<void, void>::delegate_t::from_method<CMissionManager, &CMissionManager::keepAliveHandler>( this ) ),"
                      "m_missionListCallback(airware::airmail::CServiceDelegate<void, CMissionList>::delegate_t::from_method<CMissionManager, &CMissionManager::missionListHandler>( this ) )" )

stub.stubConstructor( "COperatorModule", "",
                      "CManeuverSource( ControlRequest_controlRequestorType_OPERATOR_MODULE ),"
                      "m_rcCommandTopic( \"airware.RcInputMsg\" ),"
                      "m_rcCommandCallback(airware::airmail::CTopicDelegate<CRcInputMsg>::delegate_t::from_method<COperatorModule, &COperatorModule::rcCommandHandler>( this ) )" )

stub.stubConstructor( "CManeuverSource", "ControlRequest_controlRequestorType",
                      "m_maneuverRequestSvc( \"airware.maneuverRequestSvc\" ),"
                      "m_maneuverControlRequestSvc( \"airware.maneuverControlRequestSvc\" ),"
                      "m_activeManeuverSourceNotificationTopic( \"airware.activeManeuverSourceNotification\" ),"
                      "m_maneuverExecutionStatusTopic( \"airware.maneuverExecutionStatusEvent\" ),"
                      "m_maneuverSourceNotificationCallback(airware::airmail::CTopicDelegate<CActiveControlSourceNotification>::delegate_t::from_method<CManeuverSource, &CManeuverSource::activeManeuverSourceNotificationHandler>( this ) ),"
                      "m_maneuverStatusCallback(airware::airmail::CTopicDelegate<CManeuverExecutionStatus>::delegate_t::from_method<CManeuverSource, &CManeuverSource::maneuverStatusNotificationHandler>( this ) )")

# Destructors
stub.stubDestructor( "CContingencyManager" )
stub.stubDestructor( "CMissionManager" )
stub.stubDestructor( "COperatorModule" )
stub.stubDestructor( "CManeuverSource" )

# Thread Worker Functions
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CContingencyManager::onStart" )
stub.stubFunction( ("void",), "CContingencyManager::onLoop" )

stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CMissionManager::onStart" )
stub.stubFunction( ("void",), "CMissionManager::onLoop" )

stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "COperatorModule::onStart" )
stub.stubFunction( ("void",), "COperatorModule::onLoop" )

stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CManeuverSource::onStart" )
stub.stubFunction( ("void",), "CManeuverSource::onLoop" )

# Airmail subscription handlers
stub.stubFunction( ("void",""), "CContingencyManager::activeManeuverSourceNotificationHandler", "const CActiveControlSourceNotification&", "const airware::airmail::CEventInfo &" )
stub.stubFunction( ("void",""), "CContingencyManager::maneuverStatusNotificationHandler", "const CManeuverExecutionStatus&", "const airware::airmail::CEventInfo &" )
stub.stubFunction( ("void",""), "CContingencyManager::rcCommandHandler", "const CRcInputMsg&", "const airware::airmail::CEventInfo &" )

stub.stubFunction( ("void",""), "CMissionManager::activeManeuverSourceNotificationHandler", "const CActiveControlSourceNotification&", "const airware::airmail::CEventInfo &" )
stub.stubFunction( ("void",""), "CMissionManager::maneuverStatusNotificationHandler", "const CManeuverExecutionStatus&", "const airware::airmail::CEventInfo &" )

stub.stubFunction( ("void",""), "CManeuverSource::activeManeuverSourceNotificationHandler", "const CActiveControlSourceNotification&", "const airware::airmail::CEventInfo &" )
stub.stubFunction( ("void",""), "CManeuverSource::maneuverStatusNotificationHandler", "const CManeuverExecutionStatus&", "const airware::airmail::CEventInfo &" )

# Airmail service handlers
stub.stubFunction( ("int32_t","0"), "CContingencyManager::missionUploadHandler", "const CMission&", "CMission*" )
stub.stubFunction( ("int32_t","0"), "CContingencyManager::maneuverUploadHandler", "const CManeuver&" )
stub.stubFunction( ("int32_t","0"), "CContingencyManager::maneuverDownloadHandler", "const CManeuver&", "CManeuver*" )
stub.stubFunction( ("int32_t","0"), "CContingencyManager::missionListHandler", "CMissionList*" )
stub.stubFunction( ("int32_t","0"), "CContingencyManager::missionDownloadHandler", "const CMission&", "CMission*" )

stub.stubFunction( ("int32_t","0"), "CMissionManager::missionUploadHandler", "const CMission&", "CMission*" )
stub.stubFunction( ("int32_t","0"), "CMissionManager::maneuverUploadHandler", "const CManeuver&" )
stub.stubFunction( ("int32_t","0"), "CMissionManager::maneuverDownloadHandler", "const CManeuver&", "CManeuver*" )
stub.stubFunction( ("int32_t","0"), "CMissionManager::missionListHandler", "CMissionList*" )
stub.stubFunction( ("int32_t","0"), "CMissionManager::missionDownloadHandler", "const CMission&", "CMission*" )
stub.stubFunction( ("int32_t","0"), "CMissionManager::missionControlRequestHandler", "const CControlRequest&" )
stub.stubFunction( ("int32_t","0"), "CMissionManager::keepAliveHandler" )
stub.stubFunction( ("int32_t","0"), "CMissionManager::missionExecHandler", "const CMissionExec&" )

stub.stubFunction( ("void",""), "COperatorModule::activeManeuverSourceNotificationHandler", "const CActiveControlSourceNotification&", "const airware::airmail::CEventInfo &" )
stub.stubFunction( ("void",""), "COperatorModule::rcCommandHandler", "const CRcInputMsg&", "const airware::airmail::CEventInfo &" )

# Functions
stub.stubConstFunction( ("bool","true"), "CContingencyManager::areContingenciesLoaded" )
