import sys
from genStubs import *

stub = Stubs( "CCameraStatusThread", sys.argv[1], sys.argv[2] )

stub.include("actuator/CCameraStatusThread.h")
stub.newline()

stub.addLine("namespace airware")
stub.addLine("{")
stub.addLine("namespace actuatorSat")
stub.addLine("{")

stub.addLine("static CCameraStatusThread  *pTheCameraStatusThread = NULL;")
stub.addLine("static uint32_t              theCameraStatusThreadMem[ SIZEOF_WORDS( airware::actuatorSat::CCameraStatusThread ) ];")
stub.addLine("CCameraStatusThread &theCameraStatusThread( void )")
stub.addLine("{")
stub.addLine("    if( pTheCameraStatusThread == NULL ) {")
stub.addLine("        pTheCameraStatusThread = new( theCameraStatusThreadMem ) CCameraStatusThread();")
stub.addLine("    }")
stub.addLine("    return *pTheCameraStatusThread;")
stub.addLine("}")


stub.stubConstructor( "CCameraStatusThread", "void", "m_minPulseWidthFastTicks( 0 )",
                     "m_lastEdgeWasRising( false )",
                     "m_activeHighPulse( true )",
                     "m_lastTime_fastTicks( 0 )",
                     "m_lastDetection_slowTicks( 0 )",
                     "m_picCtr( 0 )",
                     "m_postPicDetectedErr( false )",
                     "m_pictureTakenTopic( \"airware.pictureTaken\" )"
                     )
stub.addLine("}")
stub.addLine("}")

stub.stubFunction( ("bool","true"), "airware::actuatorSat::CCameraStatusThread::init" )
stub.stubFunction( ("void",), "airware::actuatorSat::CCameraStatusThread::setDetectionPolarity", "const bool" )
stub.stubFunction( ("bool","true"), "airware::actuatorSat::CCameraStatusThread::onEnable" )
stub.stubFunction( ("void",), "airware::actuatorSat::CCameraStatusThread::onDisable" )
stub.stubFunction( ("void",), "airware::actuatorSat::CCameraStatusThread::mainLoop" )
stub.stubFunction( ("void",), "airware::actuatorSat::CCameraStatusThread::edgeDetected" )
stub.stubFunction( ("void",), "airware::actuatorSat::CCameraStatusThread::picDetected" )

stub.stubFunction( ("void",), "airware::actuatorSat::pictureTakenISR")

# stub.addLine("}")
# stub.addLine("}")

