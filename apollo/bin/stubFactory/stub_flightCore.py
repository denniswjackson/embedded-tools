import sys
from genStubs import *

stub = Stubs( "flightCore", sys.argv[1], sys.argv[2] )


stub.include( "flightCore/CControllerIfc.h" )
stub.include( "flightCore/CFastControlThread.h" )
stub.include( "flightCore/CFlightCoreCfgApi.h" )
stub.include( "flightCore/CFlightCoreStateMachine.h" )
stub.include( "flightCore/CPressurePublisher.h" )
stub.newline()

stub.useNamespace( "airware::flightCore" )
stub.useNamespace( "airware::uios" )
stub.newline()

# Singletons
stub.addLine( "CFlightCoreCfgApi       g_CFlightCoreCfgApi_instance;" )
stub.addLine( "CFlightCoreStateMachine g_CFlightCoreStateMachine_instance;" )
stub.addLine( "CControllerIfc          g_CControllerIfc_instance;" )
stub.newline()

stub.stubFunction( ("CFlightCoreCfgApi&","g_CFlightCoreCfgApi_instance"), "CFlightCoreCfgApi::theFlightCoreCfgApi" )
stub.stubFunction( ("CFlightCoreStateMachine&","g_CFlightCoreStateMachine_instance"), "CFlightCoreStateMachine::theStateMachine" )
stub.stubFunction( ("CControllerIfc&","g_CControllerIfc_instance"), "CControllerIfc::theController" )

# Constructors
stub.stubConstructor( "CControllerIfc", "" )
stub.stubConstructor( "CControllerParams", "" )
stub.stubConstructor( "CManExParams", "" )
stub.stubConstructor( "CManeuverExecutorIfc", "" )
stub.stubConstructor( "CFlightCoreStateMachine", "",
                      "m_setSystemModeSvc( \"airware.setSystemMode\" ),"
                      "m_getSystemModeSvc( \"airware.getSystemMode\" ),"
                      "m_systemModeTopic( \"airware.systemModeAnnounce\" ),"
                      "m_systemModeGCSTopic( \"flightStatus\" ),"
                      "m_uptimeGCSTopic( \"boardStatus\" )" )
stub.stubConstructor( "CFastControlThread", "",
                      "m_aeroTerminateRequestSvc( \"airware.x\" ),"
                      "m_inTerminateState( false ),"
                      "m_pubErr( airware::airmail::AIRMAIL_OK )" )
stub.stubConstructor( "CImuPublisher", "",
                      "m_accelGyroDataTopic( \"imu\" ),"
                      "m_accelGyroDataRawTopic( \"raw\" )" )
stub.stubConstructor( "CPressurePublisher", "",
                      "m_pressureTopic( \"prs\" ),"
                      "m_temperatureTopic( \"tmp\" )" )
stub.stubConstructor( "CFlightCoreCfgApi", "",
                      "m_setAttCtrlConfigSvc( \"airware.setAttCtrlConfig\" ),"
                      "m_getAttCtrlConfigSvc( \"airware.getAttCtrlConfig\" ),"
                      "m_setPosVelCtrlConfigSvc( \"airware.setPosVelCtrlConfig\" ),"
                      "m_getPosVelCtrlConfigSvc( \"airware.getPosVelCtrlConfig\" ),"
                      "m_setGuidanceConfigSvc( \"airware.setGuidanceConfig\" ),"
                      "m_getGuidanceConfigSvc( \"airware.getGuidanceConfig\" ),"
                      "m_setPrimaryControlMixSvc( \"airware.setPrimaryControlMix\" ),"
                      "m_getPrimaryControlMixSvc( \"airware.getPrimaryControlMix\" ),"
                      "m_setEffectorSurfaceMapSvc( \"airware.setEffectorSurfaceMap\" ),"
                      "m_getEffectorSurfaceMapSvc( \"airware.getEffectorSurfaceMap\" ),"
                      "m_setTelemetryWatchdogConfigSvc( \"airware.setTelemetryWatchdogConfig\" ),"
                      "m_getTelemetryWatchdogConfigSvc( \"airware.getTelemetryWatchdogConfig\" ),"
                      "m_setMPUCalService( \"airware.sensors.MPUCalSetConfig\" ),"
                      "m_getMPUCalService( \"airware.sensors.MPUCalGetConfig\" ),"
                      "m_setIMUOrientationConfigService( \"airware.sensors.IMUOrientationSetConfig\" ),"
                      "m_getIMUOrientationConfigService( \"airware.sensors.IMUOrientationGetConfig\" ),"
                      "m_setINSConfigSvc( \"airware.nav.setINSConfig\" ),"
                      "m_getINSConfigSvc( \"airware.nav.getINSConfig\" ),"
                      "m_setRcChannelMapConfigSvc( \"airware.OMSetRcChannelMapConfig\" ),"
                      "m_getRcChannelMapConfigSvc( \"airware.OMGetRcChannelMapConfig\" ),"
                      "m_setOperatorModuleConfigSvc( \"airware.setOperatorModuleConfig\" ),"
                      "m_getOperatorModuleConfigSvc( \"airware.getOperatorModuleConfig\" ),"
                      "m_setPowerMonitorConfigSvc( \"airware.setPowerManagerConfig\" ),"
                      "m_getPowerMonitorConfigSvc( \"airware.getPowerManagerConfig\" ),"
                      "m_setVehicleDescriptionConfigSvc( \"airware.setVehicleDescription\" ),"
                      "m_getVehicleDescriptionConfigSvc( \"airware.getVehicleDescription\" ),"
                      "m_setContingencyEventMapConfigSvc( \"airware.setContingencyEventMapConfig\" ),"
                      "m_getContingencyEventMapConfigSvc( \"airware.getContingencyEventMapConfig\" ),"
                      "m_saveConfigSvc( \"airware.saveConfig\" ),"
                      "m_setControlLogRateConfigSvc( \"airware.control.setControlLogRateConfig\" ),"
                      "m_getControlLogRateConfigSvc( \"airware.control.getControlLogRateConfig\" ),"
                      "m_OMattCtrlConfigSvc( \"airware.OMAttCtrlConfig\" ),"
                      "m_OMposVelCtrlConfigSvc( \"airware.OMPosVelCtrlConfig\" )" )

#Functions
stub.stubFunction( ("bool","true"), "CFlightCoreStateMachine::mayAccessConfig" )
stub.stubFunction( ("bool","true"), "CFlightCoreStateMachine::mayPerformActiveControl" )
stub.stubFunction( ("bool","true"), "CFlightCoreStateMachine::mayReboot" )
stub.stubFunction( ("bool","true"), "CFlightCoreStateMachine::mayEnforceTiming" )
stub.stubFunction( ("bool","false"), "CFlightCoreStateMachine::isInAir" )

stub.stubFunction( ("bool","true"), "CFlightCoreCfgApi::areTuningParamsChanged" )

stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CFastControlThread::onStart" )
stub.stubFunction( ("void",""), "CFastControlThread::onLoop" )
stub.stubFunction( ("void",""), "CFastControlThread::publishAirmailData" )
stub.stubFunction( ("void",""), "CFastControlThread::pollKillSignal" )
stub.stubFunction( ("void",""), "CFastControlThread::checkTerminateAndKill" )
stub.stubFunction( ("bool","true"), "CFastControlThread::init" )

stub.stubFunction( ("bool","true"), "CPressurePublisher::init" )
stub.stubFunction( ("void",""), "CPressurePublisher::update" )
stub.stubFunction( ("void",""), "CPressurePublisher::readTempPresWrapper", "int32_t*", "int32_t*" )

stub.stubFunction( ("bool","true"), "CImuPublisher::init" )
stub.stubFunction( ("bool","true"), "CImuPublisher::regAirmail" )
stub.stubFunction( ("const CAccelGyroDataMsg*","NULL"), "CImuPublisher::waitForImuMeasurement" )
stub.stubFunction( ("void",""), "CImuPublisher::publishImuData" )
stub.stubFunction( ("void",""), "CImuPublisher::checkForImuErrors" )
stub.stubFunction( ("bool","true"), "CImuPublisher::getSensorData" )

stub.stubFunction( ("maneuverReturn_t","maneuverReturn_t_ACCEPTED"), "CManeuverExecutorIfc::validateManeuver", "const CManeuver *const", "const bool" )
