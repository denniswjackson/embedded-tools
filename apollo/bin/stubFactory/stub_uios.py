import sys
from genStubs import *

stub = Stubs( "uios", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "uios/CMsgQueue.h" )
stub.include( "uios/CThreadWorker.h" )
stub.include( "uios/CThreadInfo.h" )
stub.include( "uios/CSemaphore.h" )
stub.include( "uios/CCircularByteBuffer.h")
stub.include( "uios/CUart.h" )
stub.include( "uios/CUiosScopedMutex.h" )
stub.include( "uios/osSupport.h" )
stub.include( "uios/uiosTime.h" )
stub.include( "uios/osSupport.h" )
stub.include( "uios/simTime.h" )
stub.include( "uios/socket.h" )
stub.include( "uios/uiosStdio.h" )
stub.newline()

### Used Namespaces
stub.useNamespace( "airware" )
stub.useNamespace( "airware::uios" )
stub.newline()

### Constructors/Destructors
# CThreadInfo
stub.stubConstructor( "CThreadInfo", "CThreadList *pList, IThreadWorker::threadPriority_t Priority, IThreadWorker *pThread" )
stub.stubDestructor( "CThreadInfo" )
stub.stubConstructor( "CMsgQueue", "void**, uint8_t" )
stub.stubDestructor( "CMsgQueue" )

# CThreadWorker
stub.stubConstructor( "CThreadWorker", "const char *" )
stub.stubConstructor( "CThreadWorker", "" )
stub.stubDestructor( "CThreadWorker" )

# CSemaphore
stub.stubConstructor( "CSemaphore", "" )
stub.stubDestructor( "CSemaphore" )

# CMutex
stub.stubConstructor( "CMutex", "" )
stub.stubDestructor( "CMutex" )

# CCircularByteBuffer
stub.stubConstructor( "CCircularByteBuffer", "uint8_t *arg1, size_t arg2", "m_pData(arg1)", "m_capacity(arg2)" )
stub.stubDestructor( "CCircularByteBuffer" )

# CRunningStat
stub.stubConstructor( "CRunningStat", "" )

stub.stubFunction( ("void",""), "CRunningStat::init" )
stub.stubFunction( ("bool","true"), "CRunningStat::pushf", "const float" )
stub.stubConstFunction( ("uint32_t","0"), "CRunningStat::getNumValues" )
stub.stubConstFunction( ("float","0.0F"), "CRunningStat::getMaxf" )
stub.stubConstFunction( ("float","0.0F"), "CRunningStat::getMinf" )
stub.stubConstFunction( ("float","0.0F"), "CRunningStat::getMeanf" )
stub.stubConstFunction( ("float","0.0F"), "CRunningStat::getVarf" )
stub.stubConstFunction( ("float","0.0F"), "CRunningStat::getStdf" )

### Member Functions
# CThreadWorker
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::launch" )
stub.stubOverload( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::launch", "CThreadWorker_launchOverload", "uint32_t*", "uint32_t", "IThreadWorker::threadPriority_t" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::waitOnStart", "uint32_t" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::stop" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::join" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::setPriority", "IThreadWorker::threadPriority_t" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::setStack", "uint32_t *", "uint32_t" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::onStart" )
stub.stubFunction( ("IThreadWorker::threadStatus_t","IThreadWorker::TW_OK"), "CThreadWorker::onStop" )
stub.stubFunction( ("void",), "CThreadWorker::setName", "const char *" )
stub.stubConstFunction( ("const char *","\"test\""), "CThreadWorker::getName" )
stub.stubFunction( ("CThreadWorker::threadId_t","0"), "CThreadWorker::translatePriorityToId", "IThreadWorker::threadPriority_t" )

# CSemaphore
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CSemaphore::init", "unsigned int" )
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CSemaphore::wait", "unsigned short" )
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CSemaphore::tryTake" )
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CSemaphore::take" )
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CSemaphore::give" )
stub.stubFunction( ("void",), "CSemaphore::close" )
stub.stubConstFunction( ("bool","true"), "CSemaphore::isInitialized" )

# CMutex
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CMutex::init" )
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CMutex::give" )
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CMutex::take" )
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CMutex::tryTake" )
stub.stubFunction( ("ILock::lockStatus_t","ILock::LOCK_OK"), "CMutex::wait", "unsigned short" )
stub.stubFunction( ("void",), "CMutex::close" )

# Internal scoped locks
stub.stubConstructor( "CUiosScopedMutex", "CMutex*" )
stub.stubDestructor( "CUiosScopedMutex" )

# CUart
stub.stubConstructor( "CUart", "const char *" )
stub.stubConstructor( "CUart", "const char *, uint32_t" )
stub.stubDestructor( "CUart" )
stub.stubFunction( ("size_t","0"), "CUart::read", "uint8_t *", "size_t" )
stub.stubFunction( ("IDataSource::sourceStatus_t","IDataSource::SOURCE_OK"), "CUart::readBlocking", "uint8_t *", "size_t", "size_t *", "uint16_t" )
stub.stubFunction( ("IDataSource::sourceStatus_t","IDataSource::SOURCE_OK"), "CUart::setSourceFlags", "uint16_t" )
stub.stubFunction( ("IDataSink::sinkStatus_t","IDataSink::SINK_OK"), "CUart::write", "const uint8_t *", "size_t" )
stub.stubFunction( ("IDataSink::sinkStatus_t","IDataSink::SINK_OK"), "CUart::writeBlocking", "const uint8_t *", "size_t", "uint16_t" )
stub.stubFunction( ("IUart::uartStatus_t","IUart::UART_OK"), "CUart::setBaudRate", "const uint32_t" )
stub.stubFunction( ("IUart::uartStatus_t","IUart::UART_OK"), "CUart::setDataBits", "const IUart::uartDataBits_t" )
stub.stubFunction( ("IUart::uartStatus_t","IUart::UART_OK"), "CUart::setParity", "const IUart::uartParity_t" )
stub.stubFunction( ("IUart::uartStatus_t","IUart::UART_OK"), "CUart::setStopBits", "const IUart::uartStopBits_t" )
stub.stubFunction( ("IUart::uartStatus_t","IUart::UART_OK"), "CUart::setFlowControl", "const IUart::uartFlowControl_t" )
stub.stubFunction( ("IUart::uartStatus_t","IUart::UART_OK"), "CUart::setLineDriverMode", "const IUart::uartLineDriverMode_t" )
stub.stubFunction( ("IUart::uartStatus_t","IUart::UART_OK"), "CUart::enable" )
stub.stubFunction( ("IUart::uartStatus_t","IUart::UART_OK"), "CUart::disable" )
stub.stubFunction( ("uint32_t","IUart::UART_OK"), "CUart::getBaudRate" )
stub.stubFunction( ("IUart::uartDataBits_t","IUart::UART_8_BITS"), "CUart::getDataBits" )
stub.stubFunction( ("IUart::uartParity_t","IUart::UART_NO_PARITY"), "CUart::getParity" )
stub.stubFunction( ("IUart::uartStopBits_t","IUart::UART_ONE_STOP"), "CUart::getStopBits" )
stub.stubFunction( ("IUart::uartFlowControl_t","IUart::UART_NO_FLOW_CONTROL"), "CUart::getFlowControl" )
stub.stubFunction( ("IUart::uartLineDriverMode_t","IUart::UART_LINE_DRIVER_RAW"), "CUart::getLineDriverMode" )
stub.stubConstFunction( ("uint16_t","0"), "CUart::getSourceFlags" )
stub.stubFunction( ("bool","true"), "CUart::isEnabled" )
stub.stubFunction( ("bool","true"), "CUart::startModule" )
stub.stubFunction( ("bool","true"), "CUart::stopModule" )

# CMsgQueue
stub.stubFunction( ("void*","NULL"), "CMsgQueue::pend", "int" )
stub.stubFunction( ("bool","true"), "CMsgQueue::post", "void*" )
stub.stubFunction( ("msgQueueStatus_t*","NULL"), "CMsgQueue::status" )

### CCircularByteBuffer
stub.stubConstFunction( ("size_t", "0"), "CCircularByteBuffer::size" )
stub.stubConstFunction( ("size_t", "0"), "CCircularByteBuffer::spaceAvailable" )
stub.stubFunction( ("void",), "CCircularByteBuffer::push_front", "const uint8_t *", "size_t" )
stub.stubFunction( ("bool", "true"), "CCircularByteBuffer::pop_back", "uint8_t *", "size_t" )
stub.stubFunction( ("void",), "CCircularByteBuffer::clear" )

### Global Functions
stub.stubFunction( ("void",), "airware::uios::sleep_TICKS", "uint16_t" )
stub.stubFunction( ("void",), "airware::uios::sleep_MS", "uint16_t" )
stub.stubFunction( ("uint32_t","0"), "airware::uios::getTime_TICKS" )
stub.stubOverload( ("uint32_t","0"), "airware::uios::getTime_TICKS", "airware_uios_getTime_Overload", "uiosClock_t" )
stub.stubFunction( ("void",), "airware::uios::setOsInitialized", "bool" )
stub.stubFunction( ("bool","true"), "airware::uios::useSimTime", "bool" )
stub.stubFunction( ("void",""), "airware::uios::setTime_TICKS", "uint32_t" )

stub.stubFunction( ("UIOS_FILE*","NULL"), "airware::uios::uios_fopen", "char const *", "char const *" )
stub.stubFunction( ("int","0"), "airware::uios::uios_fclose", "UIOS_FILE * const" )
stub.stubFunction( ("size_t","0"), "airware::uios::uios_fread", "void * const", "size_t", "size_t", "UIOS_FILE * const" )
stub.stubFunction( ("uint32_t","0"), "airware::uios::uios_fwrite", "const void *", "size_t", "size_t", "UIOS_FILE * const" )
stub.stubFunction( ("int","0"), "airware::uios::uios_fseek", "UIOS_FILE * const", "long int", "int" )
stub.stubFunction( ("int","0"), "airware::uios::uios_fflush", "UIOS_FILE * const" )
stub.stubFunction( ("int","0"), "airware::uios::uios_feof", "UIOS_FILE * const" )
stub.stubFunction( ("int","0"), "airware::uios::uios_ferror", "UIOS_FILE * const" )
stub.stubFunction( ("int","0"), "airware::uios::uios_setvbuf", "UIOS_FILE * const", "char * const", "int", "size_t" )
stub.stubFunction( ("uint32_t","0"), "airware::uios::uios_sync" )
stub.stubFunction( ("int","0"), "airware::uios::uios_chdir", "const char *" )
stub.stubFunction( ("int","0"), "airware::uios::uios_mkdir", "const char *" )
stub.stubFunction( ("int","0"), "airware::uios::uios_remove", "const char *" )
stub.stubFunction( ("bool","false"), "airware::uios::uios_isDir", "const char *" )
stub.stubFunction( ("int","0"), "airware::uios::uios_readdir_r", "UIOS_DIR *", "struct uios_dirent *", "struct uios_dirent **" )
stub.stubFunction( ("UIOS_DIR*","NULL"), "airware::uios::uios_opendir", "const char *" )
stub.stubFunction( ("int","0"), "airware::uios::uios_closedir", "UIOS_DIR *" )
stub.stubFunction( ("int","0"), "airware::uios::uios_volumeInfo", "uios_volume_info *" )
stub.stubFunction( ("int","0"), "airware::uios::uios_formatNand" )
stub.stubFunction( ("int","0"), "airware::uios::socket", "int", "int", "int" )
stub.stubFunction( ("int","0"), "airware::uios::closeSocket", "int" )

### Global Variables
stub.addLine( "const uint16_t airware::uios::TICKS_PER_MS = 1;" )
stub.addLine( "const uint16_t airware::uios::WAIT_FOREVER = 1;" )
