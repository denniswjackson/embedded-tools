import sys
from genStubs import *

stub = Stubs( "jsbsim", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "uios/CThreadWorker.h" )
stub.include( "models/FGFCS.h" )
stub.include( "models/FGAtmosphere.h" )
stub.include( "models/FGAuxiliary.h" )
stub.include( "models/FGPropulsion.h" )
stub.include( "models/FGPropagate.h" )
stub.include( "FGJSBBase.h" )
stub.include( "FGFDMExec.h" )
stub.newline()

### Used Namespaces
stub.useNamespace( "JSBSim" )
stub.newline()

### Constructors/Destructors
# CThreadInfo
stub.stubConstructor( "FGInitialCondition", "FGFDMExec*" )
stub.stubConstructor( "FGModel", "FGFDMExec*" )
stub.stubConstructor( "FGPropagate", "FGFDMExec *pExec",
                      "FGModel( pExec )" )
stub.stubConstructor( "FGFCS", "FGFDMExec *pExec",
                      "FGModel( pExec )" )
stub.stubConstructor( "FGAuxiliary", "FGFDMExec *pExec",
                      "FGModel( pExec )" )
stub.stubConstructor( "FGAtmosphere", "FGFDMExec *pExec",
                      "FGModel( pExec ),SutherlandConstant(0.0),Beta(0.0)" )
stub.stubConstructor( "FGQuaternion", "const FGQuaternion&" )
stub.stubConstructor( "FGColumnVector3", "" )
stub.stubConstructor( "FGMatrix33", "" )
stub.stubConstructor( "FGLocation", "" )

# Constructor supplied by application since it needs to initialize some internals
stub.stubDestructor( "FGInitialCondition" )
stub.stubDestructor( "FGPropagate" )
stub.stubDestructor( "FGModel" )
stub.stubDestructor( "FGModelFunctions" )
stub.stubDestructor( "FGAtmosphere" )
stub.stubDestructor( "FGAuxiliary" )
stub.stubDestructor( "FGFCS" )

### Member Functions
stub.stubFunction( ("void",""), "FGPropagate::DumpState" )
stub.stubFunction( ("bool","true"), "FGFDMExec::Run" )
stub.stubFunction( ("bool","true"), "FGFDMExec::RunIC" )
stub.stubFunction( ("bool","true"), "FGModelFunctions::InitModel" )
stub.stubFunction( ("bool","true"), "FGPropagate::Run", "bool" )
stub.stubFunction( ("void",""), "FGPropagate::Debug", "int" )
stub.stubFunction( ("bool","true"), "FGAuxiliary::Run", "bool" )
stub.stubFunction( ("void",""), "FGAuxiliary::Debug", "int" )
stub.stubFunction( ("bool","true"), "FGFCS::InitModel" )
stub.stubFunction( ("bool","true"), "FGFCS::Run", "bool" )
stub.stubFunction( ("void",""), "FGFCS::Debug", "int" )
stub.stubFunction( ("bool","true"), "FGModel::InitModel" )
stub.stubFunction( ("bool","true"), "FGModel::Run", "bool" )
stub.stubFunction( ("bool","true"), "FGAtmosphere::Run", "bool" )
stub.stubFunction( ("void",""), "FGAtmosphere::Debug", "int" )
stub.stubFunction( ("void",""), "FGAtmosphere::bind" )
stub.stubFunction( ("void",""), "FGModel::Debug", "int" )
stub.stubFunction( ("void",""), "FGFCS::SetThrottleCmd", "int", "double" )
stub.stubFunction( ("bool", "true"), "FGFDMExec::LoadScript", "const std::string&", "double", "const std::string" )
stub.stubFunction( ("bool", "true"), "FGModelFunctions::Load", "Element *","FGPropertyManager *","std::string" )

stub.stubFunction( ("void",""), "FGJSBBase::ProcessMessage" )
stub.stubFunction( ("void",""), "FGInitialCondition::SetAltitudeAGLFtIC", "double" )
stub.stubFunction( ("void",""), "FGInitialCondition::SetTerrainElevationFtIC", "double" )
stub.stubFunction( ("void",""), "FGInitialCondition::SetLatitudeRadIC", "double" )
stub.stubFunction( ("void",""), "FGInitialCondition::SetLongitudeRadIC", "double" )
stub.stubFunction( ("void",""), "FGInitialCondition::SetEulerAngleRadIC", "int", "double" )
stub.stubFunction( ("void",""), "FGInitialCondition::SetNEDVelFpsIC", "int", "double" )
stub.stubFunction( ("void",""), "FGAtmosphere::SetTemperatureSL", "double", "FGAtmosphere::eTemperature" )
stub.stubFunction( ("void",""), "FGAtmosphere::SetPressureSL", "FGAtmosphere::ePressure", "double" )

stub.stubConstFunction( ("void",""), "FGLocation::ComputeDerivedUnconditional" )
stub.stubConstFunction( ("void",""), "FGQuaternion::ComputeDerivedUnconditional" )
stub.stubConstFunction( ("double","0.0"), "FGInitialCondition::GetAltitudeAGLFtIC" )
stub.stubConstFunction( ("double","0.0"), "FGInitialCondition::GetTerrainElevationFtIC" )
stub.stubConstFunction( ("double","0.0"), "FGAtmosphere::GetDensity", "double" )
stub.stubConstFunction( ("double","0.0"), "FGAtmosphere::ConvertToRankine", "double", "FGAtmosphere::eTemperature" )
stub.stubConstFunction( ("double","0.0"), "FGAtmosphere::ConvertToPSF", "double", "FGAtmosphere::ePressure" )
stub.stubConstFunction( ("double","0.0"), "FGAtmosphere::ConvertFromPSF", "double", "FGAtmosphere::ePressure" )

### Global Variables
stub.addLine( "short FGJSBBase::debug_lvl=0;" )
stub.addLine( "const double FGJSBBase::radtodeg=0.0;" )
stub.addLine( "const double FGJSBBase::fttom=0.0;" )
