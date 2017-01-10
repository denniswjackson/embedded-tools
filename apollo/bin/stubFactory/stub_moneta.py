import sys
from genStubs import *

stub = Stubs( "moneta", sys.argv[1], sys.argv[2] )

### Include Headers
stub.addLine( "#define private public")
stub.addLine( "#define protected public")
stub.include( "moneta/CMoneta.h" )
stub.include( "moneta/CWorkingSetFlash.h")
stub.addLine( "#undef private")
stub.addLine( "#undef protected")
stub.newline()

### Used Namespaces
stub.newline()

#### Constructors/Destructors
stub.stubConstructor( "CMoneta", "" )
stub.stubDestructor( "CMoneta" )
stub.stubDestructor( "CWorkingSet" )
stub.stubDestructor( "CWorkingSetFlash" )

# unfortunately we need constant initializers here so "stubConstructor" won't
# be sufficient:
stub.addLine("CWorkingSetFlash::CWorkingSetFlash( const uint32_t PrimarySectorAddr,")
stub.addLine("                                    const uint8_t PrimarySectorId," )
stub.addLine("                                    const uint32_t SecondarySectorAddr," )
stub.addLine("                                    const uint8_t SecondarySectorId," )
stub.addLine("                                    const uint32_t SectorSize_bytes," )
stub.addLine("                                    const uint32_t MaxWorkingSetSize_bytes):" )
stub.addLine("    m_sectorSize_bytes( SectorSize_bytes )," )
stub.addLine("    m_primarySectorAddr( PrimarySectorAddr )," )
stub.addLine("    m_primarySectorStmId( PrimarySectorId )," )
stub.addLine("    m_secondarySectorAddr( SecondarySectorAddr )," )
stub.addLine("    m_secondarySectorStmId( SecondarySectorId )," )
stub.addLine("    m_maxWorkingSetSize_bytes( MaxWorkingSetSize_bytes )," )
stub.addLine("    m_maxParamCount( ( m_maxWorkingSetSize_bytes - REGION_HEADER_SIZE_BYTES ) / PARAM_DATA_MIN_SIZE ) {}" )


# Singletons
stub.addLine( "CMoneta &CMoneta::instance()" )
stub.addLine( "{" )
stub.addLine( "    static CMoneta s_monetaInstance;" )
stub.addLine( "    return s_monetaInstance;" )
stub.addLine( "}" )
stub.newline()

# CMoneta class member functions
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CMoneta::addWorkingSet", "CWorkingSet *", "const uint32_t", "CWorkingSet::SParamWriteListEntry_t *", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CMoneta::init", "const SParamMetaEntry_t *", "const uint32_t", "uint8_t *", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CMoneta::readParam", "const uint32_t", "void *", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CMoneta::writeParam", "const uint32_t", "const void *", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CMoneta::beginTransaction" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CMoneta::endTransaction" )
stub.stubFunction( ( "bool", "false" ), "CMoneta::isTransactionActive" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CMoneta::enterCriticalMode" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CMoneta::exitCriticalMode" )

# CWorkingSetFlash class member functions
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CWorkingSetFlash::validate", "bool *" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CWorkingSetFlash::initialize", "const uint8_t", "const SParamMetaEntry_t *", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CWorkingSetFlash::needsUpdate", "const uint8_t", "const SParamMetaEntry_t *", "const uint32_t", "bool *" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CWorkingSetFlash::update", "const uint8_t", "const SParamMetaEntry_t *", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CWorkingSetFlash::readParam", "const SParamMetaEntry_t *", "uint8_t *", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CWorkingSetFlash::writeParams", "const CWorkingSet::SParamWriteListEntry_t *", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CWorkingSetFlash::setSectorBaseAddress", "const uint32_t", "const uint32_t" )
stub.stubFunction( ( "MonetaErr_t", "MONETA_ERR_NONE" ), "CWorkingSetFlash::destroy" )