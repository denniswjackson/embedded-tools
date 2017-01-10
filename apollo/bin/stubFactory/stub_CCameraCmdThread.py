import sys
from genStubs import *

stub = Stubs( "CCameraCmdThread", sys.argv[1], sys.argv[2] )

stub.include("actuator/CCameraCmdThread.h")
stub.newline()

stub.useNamespace( "airware::airmail" )

stub.addLine("namespace airware")
stub.addLine("{")
stub.addLine("namespace actuatorSat")
stub.addLine("{")

stub.addLine("static CCameraCmdThread  *pTheCameraCmdThread = NULL;")
stub.addLine("static uint32_t              theCameraCmdThreadMem[ SIZEOF_WORDS( airware::actuatorSat::CCameraCmdThread ) ];")
stub.addLine("CCameraCmdThread &theCameraCmdThread( void )")
stub.addLine("{")
stub.addLine("    if( pTheCameraCmdThread == NULL ) {")
stub.addLine("        pTheCameraCmdThread = new( theCameraCmdThreadMem ) CCameraCmdThread();")
stub.addLine("    }")
stub.addLine("    return *pTheCameraCmdThread;")
stub.addLine("}")


stub.stubConstructor( "CCameraCmdThread", "void", "m_timeouts( 0 )",
                     "m_cameraType( CAMERA_TYPE_NONE )",
                     "m_takePictureSvc( \"airware.takePictureSvc\" )",
                     "m_takePictureMsgTopic( \"airware.takePicture\" )"
                     )
stub.addLine("}")
stub.addLine("}")

stub.stubFunction( ("bool","true"), "airware::actuatorSat::CCameraCmdThread::init" )
stub.stubFunction( ("void",), "airware::actuatorSat::CCameraCmdThread::setCameraType", "airware::actuatorSat::cameraType_t" )
stub.stubFunction( ("bool","true"), "airware::actuatorSat::CCameraCmdThread::onEnable" )
stub.stubFunction( ("void",), "airware::actuatorSat::CCameraCmdThread::onDisable" )
stub.stubFunction( ("void",), "airware::actuatorSat::CCameraCmdThread::mainLoop" )

stub.stubFunction( ("void",), "airware::actuatorSat::CCameraCmdThread::takePicture", "const CActuatorTakePictureMsg &", "const CEventInfo &" )
# stub.stubFunction( ("void",), "airware::actuatorSat::CCameraCmdThread::picDetected" )

stub.stubFunction( ("void",), "airware::actuatorSat::CCameraCmdThread::pictureTimeout")

# stub.addLine("}")
# stub.addLine("}")

