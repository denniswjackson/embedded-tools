import sys
from genStubs import *

stub = Stubs( "common", sys.argv[1], sys.argv[2] )

stub.include( "common/CSatCore.h" )
stub.include( "common/CModuleLedThread.h" )
stub.include( "common/CModuleStateMachine.h" )
stub.include( "common/CResourceMonitor.h" )
stub.include( "common/CTemperaturePublisher.h" )
stub.include( "common/CVersionProvider.h" )
stub.include( "common/micrium_core.h" )
stub.include( "common/CScopedMutex.h" )
stub.include( "common/CScopedSemaphore.h" )
stub.include( "airmail/airmail.h" )
stub.newline()

stub.useNamespace( "airware"            )
stub.useNamespace( "airware::commonSat" )
stub.useNamespace( "airware::uios"      )
stub.useNamespace( "airware::airmail"   )
stub.newline()

stub.addLine( "const uint8_t  airware::commonSat::VERSION_MAJOR = 200;" )
stub.addLine( "const uint8_t  airware::commonSat::VERSION_MINOR = 201;" )
stub.addLine( "const uint8_t  airware::commonSat::VERSION_PATCH = 202;" )
stub.addLine( "const uint16_t airware::commonSat::BUILD_NUMBER = 0xFFFE;" )
stub.addLine( "const char*    airware::commonSat::COMPONENT_NAME = \"\";" )
stub.addLine( "const char*    airware::commonSat::GIT_HASH = \"\";" )
stub.newline()

# Singletons
stub.addLine( "CSatCore               g_CSatCore_theSatCore;" )
stub.addLine( "CModuleStateMachine    g_CModuleStateMachine_theStateMachine; " )
stub.addLine( "CModuleLedThread       s_theLedThread;         " )
stub.newline()

# Constructors
stub.stubConstructor( "CSatCore", "",
                      "m_requestRebootSvc( \"airware.board.reboot\" )",
                      "m_getMfgParamsSvc( \"airware.getMfgParams\" )" )
stub.stubConstructor( "CModuleStateMachine", "",
                      "m_systemModeTopic( \"airware.systemModeAnnounce\" )" )
stub.stubConstructor( "CModuleLedThread", "", "m_setLedSvc( \"airware.blinkIdLed\" )" )
stub.stubConstructor( "CResourceMonitor", "const uint32_t MaxCpu, const uint32_t MaxStack, const uint32_t MinLowWater, const uint32_t MinFree, const uint32_t MinFreeOs",
                      "m_maxCpuUtilization_PCT( MaxCpu )",
                      "m_maxStackUtilization_PCT( MaxStack )",
                      "m_threadStatsTopic( \"airware.threadStats\" )",
                      "m_minPoolLowWater_PCT( MinLowWater )",
                      "m_minPoolFree_Blocks( MinFree )",
                      "m_minOsPoolFree_PCT( MinFreeOs)",
                      "m_airmailStatsTopic( \"airware.airmailPoolStats\" )" )
stub.stubConstructor( "CTemperaturePublisher", "",
					            "m_temperatureTopic( \"\" )",
                      "m_getCoreTemperatureBiasService( \"\" )" )
stub.stubConstructor( "CVersionProvider", "", "m_svc( \"\" )")
stub.stubConstructor( "CScopedMutex", "uios::CMutex*" )
stub.stubConstructor( "CScopedSemaphore", "uios::CSemaphore*" )

stub.stubDestructor( "CScopedMutex" )
stub.stubDestructor( "CScopedSemaphore" )

#Functions
stub.stubFunction( ("bool","false"), "CSatCore::coreInit" )
stub.stubFunction( ("void",), "CSatCore::micriumInit" )
stub.stubFunction( ("uios::IThreadWorker::threadStatus_t","uios::IThreadWorker::TW_OK"), "CSatCore::onStart" )
stub.stubFunction( ("void",), "CSatCore::onLoop" )
stub.stubFunction( ("bool","false"), "CSatCore::isMicriumInitialized" )
stub.stubFunction( ("bool","false"), "CSatCore::areParamsAccessible" )
stub.stubFunction( ("bool","false"), "CSatCore::isAirmailInitialized" )
stub.stubFunction( ("RebootRequestMsg_responseCode_t","RebootRequestMsg_responseCode_t_REQUEST_GRANTED"), "CSatCore::requestReboot", "RebootRequestMsg_bootImage_t" )
stub.stubFunction( ("CSatCore&","g_CSatCore_theSatCore"), "CSatCore::theSatCore" )

stub.stubFunction( ("CModuleStateMachine&","g_CModuleStateMachine_theStateMachine"), "CModuleStateMachine::theStateMachine" )
stub.stubFunction( ("bool","true"), "CModuleStateMachine::init" )
stub.stubFunction( ("bool","true"), "CModuleStateMachine::mayAccessConfig" )
stub.stubFunction( ("bool","true"), "CModuleStateMachine::mayReboot" )
stub.stubFunction( ("bool","true"), "CModuleStateMachine::mayEnforceTiming" )
stub.stubFunction( ("CModuleStateMachine::StateTransitionErr_t","CModuleStateMachine::STATE_TRANSITION_OK"), "CModuleStateMachine::setState", "const CModuleStateMachine::ModuleState_t" )
stub.stubFunction( ("CModuleStateMachine::ModuleState_t","CModuleStateMachine::ErrorState"), "CModuleStateMachine::getState" )

stub.stubFunction( ("bool","true"), "CResourceMonitor::init" )
stub.stubFunction( ("void",), "CResourceMonitor::mainLoop" )

stub.stubFunction( ("CPUTemperatureErr_t","CPU_TEMPERATURE_ERR_NONE"), "CTemperaturePublisher::getCoreTemperatureWrapper", "float *const" )
stub.stubFunction( ("bool","true"), "CTemperaturePublisher::init" )
stub.stubFunction( ("void",), "CTemperaturePublisher::mainLoop" )

stub.stubFunction( ("bool","true"), "CVersionProvider::init" )

stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CModuleLedThread::onStart" )
stub.stubFunction( ("void",), "CModuleLedThread::setRedBlink", "bool" )
stub.stubFunction( ("void",), "CModuleLedThread::onLoop" )
stub.stubFunction( ("CModuleLedThread&","s_theLedThread"), "CModuleLedThread::theLedThread" )
