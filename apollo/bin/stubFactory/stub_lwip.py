import sys
from genStubs import *

stub = Stubs( "lwip", sys.argv[1], sys.argv[2] )

stub.include("lwipSlipIf.h")
stub.newline()

stub.externC()

stub.addLine( "typedef void ( *netifapi_void_fn )( struct netif *netif );" )
stub.addLine( "typedef err_t( *netifapi_errt_fn )( struct netif *netif );" )
stub.addLine( "typedef void ( *netifapi_void_fn )( struct netif *netif );", "h" )
stub.addLine( "typedef err_t( *netifapi_errt_fn )( struct netif *netif );", "h" )

stub.stubFunction( ("err_t", "0"), "netifapi_netif_common", "struct netif *", "netifapi_void_fn", "netifapi_void_fn" )
stub.stubFunction( ("void", ""), "netif_set_up", "struct netif *" )
stub.stubFunction( ("void", ""), "netif_set_down", "struct netif *" )
