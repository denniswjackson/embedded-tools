import sys
from genStubs import *

stub = Stubs( "micrium", sys.argv[1], sys.argv[2] )

stub.include( "ucos_ii.h" )
stub.newline()

# Everything after this call is extern "C"ed
stub.externC()
stub.include( "serial.h" )
stub.include( "fs_app.h" )
stub.newline()

stub.addLine( "INT8U OSCPUUsage;" )
stub.addLine( "OS_EVENT *OSEventFreeList = NULL;" )
stub.addLine( "OS_FLAG_GRP *OSFlagFreeList = NULL;" )
stub.addLine( "OS_TCB *OSTCBFreeList = NULL;" )
stub.addLine( "OS_MEM *OSMemFreeList = NULL;" )

stub.stubFunction( ("void",), "OSInit" )
stub.stubFunction( ("void",), "CPU_Init" )
stub.stubFunction( ("void",), "Mem_Init" )
stub.stubFunction( ("void",), "Math_Init" )
stub.stubFunction( ("void",), "OSStatInit" )
stub.stubFunction( ("INT8U","OS_ERR_NONE"), "OSTaskStkChk", "INT8U", "OS_STK_DATA*" )
stub.stubFunction( ("INT8U","OS_ERR_NONE"), "OSTaskQuery", "INT8U", "OS_TCB*" )
stub.stubFunction( ("void",), "OS_CPU_SysTickInit", "INT32U" )
stub.stubFunction( ("void",), "Serial_DevDrvAdd", "CPU_CHAR*", "SERIAL_DEV_CFG*", "CPU_SIZE_T", "CPU_SIZE_T", "SERIAL_ERR*" )

stub.stubFunction( ("CPU_BOOLEAN","DEF_OK"), "App_FS_AddNAND" )
stub.stubFunction( ("CPU_BOOLEAN","DEF_OK"), "App_FS_Init" )

stub.stubFunction( ("OS_CPU_SR", 0), "CPU_SR_Save" )
stub.stubFunction( ("void",), "CPU_SR_Restore", "OS_CPU_SR" )

stub.stubFunction( ("OS_EVENT *", "NULL"), "OSSemCreate", "uint16_t" )
stub.stubFunction( ("uint8_t", "OS_ERR_NONE"), "OSSemPost", "OS_EVENT *" )
stub.stubFunction( ("void",), "OSSemPend", "OS_EVENT *", "uint32_t", "uint8_t *" )

stub.stubFunction( ("OS_EVENT *", "NULL"), "OSMutexCreate", "uint8_t", "uint8_t *" )
stub.stubFunction( ("uint8_t", "OS_ERR_NONE"), "OSMutexPost", "OS_EVENT *" )
stub.stubFunction( ("void",), "OSMutexPend", "OS_EVENT *", "uint32_t", "uint8_t *" )