import sys
from genStubs import *

stub = Stubs( "control", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "control/controllerAutoCode.h" )
stub.include( "control/CManeuverExecutor.h" )
stub.include( "control/CManeuverValidator.h" )
stub.include( "control/controlMixer.h" )
stub.include( "control/MR_FLT_manAttitude.h" )
stub.include( "control/MR_FLT_manVelocity.h" )
stub.include( "control/MR_LND_attitudeOnly.h" )
stub.include( "systemMessages/Menagerie.pb.h" )
stub.newline()

### Used Namespaces
stub.useNamespace( "airware::control" )
stub.newline()

#### Constructors/Destructors
stub.stubConstructor( "controllerAutoCodeModelClass", "" )
stub.stubDestructor( "controllerAutoCodeModelClass" )
stub.stubConstructor( "controlMixerModelClass", "" )
stub.stubDestructor( "controlMixerModelClass" )
stub.stubConstructor( "CManeuverExecutor", "" )
stub.stubConstructor( "CManeuverValidator", "MR_FLT_manAttitudeModelClass &,\
                                             MR_FLT_manVelocityModelClass &,\
                                             MR_LND_attitudeOnlyModelClass &,\
                                             CManeuverExecutor &,\
                                             busCmdsMR_FLT_manAttitude &,\
                                             busParamsMR_FLT_manAttitude &,\
                                             busCmdsMR_FLT_manVelocity &,\
                                             busParamsMR_FLT_manVelocity &,\
                                             busParamsMR_LND_attitudeOnly &" )

#### Member Functions

## controllerAutoCodeModelClass
stub.addLine( "const busAuxCmds FlapsOff = { 0 };" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::initialize")
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::step0" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::step1" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::setpqr_meas", "float * const" )
stub.stubConstFunction( ("const float *", "NULL" ), "controllerAutoCodeModelClass::getlinearAccelCmds" )
stub.stubConstFunction( ("const float *", "NULL" ), "controllerAutoCodeModelClass::getangularAccelCmds" )
stub.stubConstFunction( ("busAuxCmds", "FlapsOff" ), "controllerAutoCodeModelClass::getauxCmds" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::setBlockParameters", "P_controllerAutoCode_T_ const *" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::setparams", "busCtrlParams" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::setINSData", "busINSData" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::setcommandData", "busCommandData" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::setcommandModes", "busCommandModes" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::setreset", "unsigned char" )
stub.stubFunction( ("void",), "controllerAutoCodeModelClass::setgyro_bias", "float * const" )
stub.addLine( "busControllerFeedback getcontrollerFeedback_default;" )
stub.stubConstFunction( ("busControllerFeedback","getcontrollerFeedback_default"), "controllerAutoCodeModelClass::getcontrollerFeedback")
stub.addLine( "busControllerInternalSignals getinternalSignals_default;" )
stub.stubConstFunction( ("busControllerInternalSignals","getinternalSignals_default"), "controllerAutoCodeModelClass::getinternalSignals")

## controlMixerModelClass
stub.stubFunction( ("void",), "controlMixerModelClass::initialize")
stub.stubFunction( ("void",), "controlMixerModelClass::step" )
stub.stubFunction( ("void",), "controlMixerModelClass::setcontrolInputs", "float * const" )
stub.stubConstFunction( ("const float *", "NULL" ), "controlMixerModelClass::geteffectorCmds" )
stub.stubConstFunction( ("boolean_T", "0" ), "controlMixerModelClass::getsaturation" )
stub.stubFunction( ("void",), "controlMixerModelClass::setBlockParameters", "P_controlMixer_T_ const *" )

# CManeuverValidator
stub.stubFunction( ("CManeuverValidator::return_t","CManeuverValidator::MANVAL_GENERIC_OK"), "CManeuverValidator::validateManeuverAndOptionallySetParams", "Maneuver const *", "bool", "bool", "bool" )

# Maneuvers

## CManeuverExecutor
stub.stubFunction( ("bool", "false" ), "CManeuverExecutor::getEnableMotors" )
stub.stubFunction( ("CManeuverExecutor::return_t", "CManeuverExecutor::MANEX_GENERIC_OK" ), "CManeuverExecutor::getParamsStore", "busCtrlParamsStore * &" )
stub.stubFunction( ("bool", "false" ), "CManeuverExecutor::checkTakePicture" )
stub.stubFunction( ("CManeuverExecutor::return_t", "CManeuverExecutor::MANEX_GENERIC_OK" ), "CManeuverExecutor::setManeuver", "tManeuverSel" )
stub.stubFunction( ("CManeuverExecutor::return_t", "CManeuverExecutor::MANEX_GENERIC_OK" ), "CManeuverExecutor::step" )
stub.stubFunction( ("CManeuverExecutor::return_t", "CManeuverExecutor::MANEX_GENERIC_OK" ), "CManeuverExecutor::setINSData", "busINSData const &" )
stub.stubFunction( ("CManeuverExecutor::return_t", "CManeuverExecutor::MANEX_GENERIC_OK" ), "CManeuverExecutor::setControllerFeedback", "busControllerFeedback const &" )
stub.addLine( "busCommandData manEx_getCommandData_default;" )
stub.stubFunction( ("busCommandData","manEx_getCommandData_default"), "CManeuverExecutor::getCommandData")
stub.addLine( "busCommandModes manEx_getCommandModes_default;" )
stub.stubFunction( ("busCommandModes","manEx_getCommandModes_default"), "CManeuverExecutor::getCommandModes")
stub.stubFunction( ("bool","false"), "CManeuverExecutor::getComplete")
stub.stubFunction( ("bool","false"), "CManeuverExecutor::isInFlight")
stub.stubFunction( ("const int *","NULL"), "CManeuverExecutor::getManeuverStateInt32Data")
stub.stubFunction( ("const float *","NULL"), "CManeuverExecutor::getManeuverStateFloatData")
stub.stubFunction( ("CManeuverExecutor::return_t", "CManeuverExecutor::MANEX_GENERIC_OK"), "CManeuverExecutor::setAGLProcIn", "CAGLMsg const &", "uint32_t" )
stub.stubFunction( ("bool","false"), "CManeuverExecutor::getRaiseAGLHealthEvent")

# Non-generic maneuvers
stub.addLine( "busCommandData MR_FLT_manAttitudeModelClass_getcommandData_default;" )
stub.stubConstFunction( ("busCommandData", "MR_FLT_manAttitudeModelClass_getcommandData_default" ), "MR_FLT_manAttitudeModelClass::getcommandData" )
stub.addLine( "busCommandModes MR_FLT_manAttitudeModelClass_getcommandModes_default;" )
stub.stubConstFunction( ("busCommandModes", "MR_FLT_manAttitudeModelClass_getcommandModes_default" ), "MR_FLT_manAttitudeModelClass::getcommandModes" )
stub.stubFunction( ("void",), "MR_FLT_manAttitudeModelClass::setINSData", "busINSData" )
stub.stubFunction( ("void",), "MR_FLT_manAttitudeModelClass::setcontrollerFeedback", "busControllerFeedback" )
stub.stubFunction( ("void",), "MR_FLT_manAttitudeModelClass::step")
stub.stubConstFunction( ("uint8_t", "0" ), "MR_FLT_manAttitudeModelClass::geteffectorEnable" )
stub.stubConstFunction( ("uint8_t", "0" ), "MR_FLT_manAttitudeModelClass::getinFlight" )
stub.stubConstructor( "MR_FLT_manAttitudeModelClass", "" )
stub.stubDestructor( "MR_FLT_manAttitudeModelClass" )

stub.addLine( "busCommandData MR_FLT_manVelocityModelClass_getcommandData_default;" )
stub.stubConstFunction( ("busCommandData", "MR_FLT_manVelocityModelClass_getcommandData_default" ), "MR_FLT_manVelocityModelClass::getcommandData" )
stub.addLine( "busCommandModes MR_FLT_manVelocityModelClass_getcommandModes_default;" )
stub.stubConstFunction( ("busCommandModes", "MR_FLT_manVelocityModelClass_getcommandModes_default" ), "MR_FLT_manVelocityModelClass::getcommandModes" )
stub.stubFunction( ("void",), "MR_FLT_manVelocityModelClass::setINSData", "busINSData" )
stub.stubFunction( ("void",), "MR_FLT_manVelocityModelClass::setcontrollerFeedback", "busControllerFeedback" )
stub.stubFunction( ("void",), "MR_FLT_manVelocityModelClass::step")
stub.stubConstFunction( ("uint8_t", "0" ), "MR_FLT_manVelocityModelClass::geteffectorEnable" )
stub.stubConstFunction( ("uint8_t", "0" ), "MR_FLT_manVelocityModelClass::getinFlight" )
stub.stubConstructor( "MR_FLT_manVelocityModelClass", "" )
stub.stubDestructor( "MR_FLT_manVelocityModelClass" )

stub.addLine( "busCommandData MR_LND_attitudeOnlyModelClass_getcommandData_default;" )
stub.stubConstFunction( ("busCommandData", "MR_LND_attitudeOnlyModelClass_getcommandData_default" ), "MR_LND_attitudeOnlyModelClass::getcommandData" )
stub.addLine( "busCommandModes MR_LND_attitudeOnlyModelClass_getcommandModes_default;" )
stub.stubConstFunction( ("busCommandModes", "MR_LND_attitudeOnlyModelClass_getcommandModes_default" ), "MR_LND_attitudeOnlyModelClass::getcommandModes" )
stub.stubConstFunction( ("uint8_t", "0" ), "MR_LND_attitudeOnlyModelClass::getcomplete" )
stub.stubFunction( ("void",), "MR_LND_attitudeOnlyModelClass::setINSData", "busINSData" )
stub.stubFunction( ("void",), "MR_LND_attitudeOnlyModelClass::setcontrollerFeedback", "busControllerFeedback" )
stub.stubFunction( ("void",), "MR_LND_attitudeOnlyModelClass::step")
stub.stubConstructor( "MR_LND_attitudeOnlyModelClass", "" )
stub.stubDestructor( "MR_LND_attitudeOnlyModelClass" )

