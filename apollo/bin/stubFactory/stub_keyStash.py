import sys
from genStubs import *

stub = Stubs( "keyStash", sys.argv[1], sys.argv[2] )

### Include Headers
stub.include( "keyStash.h" )

### Used Namespaces
stub.newline()

stub.externC()
# CMoneta class member functions
stub.stubFunction( ( "keyStashErr_t", "KEY_STASH_ERR_NONE" ), "keyStash_init", "const uint8_t * const", "const uint8_t", "const uint8_t * const", "const uint8_t", "const uint32_t", "const uint32_t", "const uint32_t" )
stub.stubFunction( ( "keyStashErr_t", "KEY_STASH_ERR_NONE" ), "keyStash_getKeyByName", "const char *", "uint8_t *", "const uint32_t", "uint32_t *" )
stub.stubFunction( ( "keyStashErr_t", "KEY_STASH_ERR_NONE" ), "keyStash_createKeyStash", "const SKeyListEntry_t *", "const uint8_t *", "const uint32_t" )
stub.stubFunction( ( "keyStashErr_t", "KEY_STASH_ERR_NONE" ), "keyStash_dev_buildKeyStashAtAddr", "const uint8_t * const", "const uint32_t", "const SKeyListEntry_t *", "const uint8_t *", "const uint32_t" );
stub.stubFunction( ( "keyStashErr_t", "KEY_STASH_ERR_NONE" ), "keyStash_dev_validateKeyStash", "const uint8_t *", "const uint32_t", "bool *", "SGlobalHeader_t *" );
stub.stubFunction( ( "keyStashErr_t", "KEY_STASH_ERR_NONE" ), "keyStash_dev_countValidKeys", "const uint8_t * const", "const uint32_t", "const uint32_t", "uint32_t *" );
