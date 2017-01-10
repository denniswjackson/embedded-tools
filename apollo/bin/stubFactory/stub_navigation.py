import sys
from genStubs import *

stub = Stubs( "navigation", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "GetEnvModelStructure.h" )
stub.include( "GetNavFilterStateStructure.h" )
stub.include( "GetFastNavOutputStructure.h" )
stub.include( "GetMedNavOutputStructure.h" )
stub.include( "NavFilterQuatPropagation.h" )

stub.include( "NavFilterCorrect.h" )
stub.include( "NavFilterPropagate.h" )
stub.include( "NavFilterInitialize.h" )
stub.include( "SetGroundAtmosphericPressure.h" )
stub.include( "SetTrueAltMSL.h" )
stub.include( "UpdateEnviornmentalModels.h" )
stub.newline()

### Used Namespaces
stub.newline()

## Dummy results
stub.addLine( "static EnvModelStruct s_EnvModelStruct;" )
stub.addLine( "static NavFilterStateStruct s_NavFilterStateStruct;" )
stub.addLine( "static FastNavOutputStruct s_FastNavOutputStruct;" )
stub.addLine( "static MedNavOutputStruct s_MedNavOutputStruct;" )
stub.addLine( "static NavFiltCorrToQuatPropStruct s_NavFiltCorrToQuatPropStruct;" )

## Functions
stub.stubFunction( ("EnvModelStruct", "s_EnvModelStruct" ), "GetEnvModelStructure" )
stub.stubFunction( ("NavFilterStateStruct", "s_NavFilterStateStruct" ), "GetNavFilterStateStructure" )
stub.stubFunction( ("FastNavOutputStruct", "s_FastNavOutputStruct" ), "GetFastNavOutputStructure" )
stub.stubFunction( ("MedNavOutputStruct", "s_MedNavOutputStruct" ), "GetMedNavOutputStructure" )
stub.stubFunction( ("NavFiltCorrToQuatPropStruct", "s_NavFiltCorrToQuatPropStruct" ), "NavFilterQuatPropagation", "IMUBaroDataStruct" )

stub.stubFunction( ("void", "" ), "NavFilterCorrect", "IMUBaroDataStruct", "GPSDataStruct", "MagDataStruct", "EnvModelStruct", "NavFiltCorrToQuatPropStruct*", "NavFiltCorrToPropStruct*", "NavPropToFiltCorrStruct*", "ResidualsStruct*" )

stub.stubFunction( ("void", "" ), "NavFilterPropagate", "IMUBaroDataStruct", "MagDataStruct", "EnvModelStruct", "uint8_t", "NavFiltCorrToPropStruct*", "NavPropToFiltCorrStruct*" )
stub.stubFunction( ("void", "" ), "NavFilterInitialize", "IMUBaroDataStruct", "GPSDataStruct", "MagDataStruct", "EnvModelStruct", "FilterConfigStruct" )
stub.stubFunction( ("void", "" ), "NavFilter_initialize" )
stub.stubFunction( ("void", "" ), "SetGroundAtmosphericPressure", "float" )
stub.stubFunction( ("void", "" ), "SetTrueAltMSL", "float" )
stub.stubFunction( ("void", "" ), "UpdateEnviornmentalModels", "float", "float", "float", "float", "uint32_t" )
