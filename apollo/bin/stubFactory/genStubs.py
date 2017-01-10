__author__ = 'jstevenson' #jstevenson says "I'm gonna save so much time, no matter how long it takes!" as he spends hours writing this module
from datetime import date
import re

class Stubs:
    # Create or overwrite stub files, adding file headers
    def __init__( self, stubbedModuleName, cppDir, hDir ):
        # Open dir/stub_<stubbedModuleName.cpp>
        self.m_module = stubbedModuleName
        self.cpp = open( cppDir + "/" + "stub_" + self.m_module + ".cpp", 'w'  )

        # Write header comment
        self.cpp.write( "/**\n" )
        self.cpp.write( "    @brief      Unit test stubs for module: %s\n" % self.m_module )
        self.cpp.write( "    @file       stub_%s.cpp\n" % self.m_module )
        self.cpp.write( "    @author     genStubs.py\n" )
        self.cpp.write( "    @copyright  Copyright (c) %s Airware. All rights reserved.\n" % date.today().year )
        self.cpp.write( "    @date       %s\n" % date.today().isoformat() )
        self.cpp.write( "*/\n" )
        self.cpp.write( "\n" )
        self.cpp.write( "#include <stdio.h> /*For NULL*/\n" )
        self.cpp.write( "#include <stdint.h> /*For uint32_t*/\n" )
        self.cpp.write( "\n" )

        # Open dir/stub_<stubbedModuleName.h>
        self.m_module = stubbedModuleName
        self.h = open( hDir + "/" + "stub_" + self.m_module + ".h", 'w'  )

        # Write header comment
        self.h.write( "/**\n" )
        self.h.write( "    @brief      Global twiddlers from unit test stubs for module: %s\n" % self.m_module )
        self.h.write( "    @file       stub_%s.h\n" % self.m_module )
        self.h.write( "    @author     genStubs.py\n" )
        self.h.write( "    @copyright  Copyright (c) %s Airware. All rights reserved.\n" % date.today().year )
        self.h.write( "    @date       %s\n" % date.today().isoformat() )
        self.h.write( "*/\n" )
        self.h.write( "#ifndef STUB_HEADER_%s\n" % self.m_module )
        self.h.write( "#define STUB_HEADER_%s\n\n" % self.m_module )

        # keep track of whether an extern C block is in progress
        self.externCed = False
        self.resetCommands = []

    def include( self, file ):
        self.cpp.write( "#include \"%s\"\n" % file )
        self.h.write( "#include \"%s\"\n" % file )

    def useNamespace( self, namespace ):
        self.cpp.write( "using namespace %s;\n" % namespace )
        self.h.write( "using namespace %s;\n" % namespace )

    def externC( self ):
        self.cpp.write( "#ifdef __cplusplus\n" )
        self.cpp.write( "extern \"C\"{\n" )
        self.h.write( "#ifdef __cplusplus\n\n" )
        self.cpp.write( "#endif\n" )
        self.h.write( "extern \"C\"{\n" )
        self.h.write( "#endif\n\n" )
        self.externCed = True

    def newline( self ):
        self.cpp.write( "\n" )
        self.h.write( "\n" )

    def addLine( self, string, location = 'cpp' ):
        if location == 'h':
            self.h.write( string + "\n" )
        elif location == 'reset':
            self.resetCommands.append( string + "\n" )
        else:
            self.cpp.write( string + "\n" )

    def stubSysMsg( self, name ):
        self.cpp.write( "%s::%s() { memset(&m_data, 0U, sizeof(m_data)); }\n" % (name, name) )
        self.stubConstFunction( ("msgSize_t","0"), "%s::getSerializedSize" % name )
        self.stubConstFunction( ("msgSize_t","0"), "%s::getMaxSerializedSize" % name )
        self.stubConstFunction( ("msgSize_t","0"), "%s::serialize" % name, "uint8_t *", "size_t" )
        self.stubFunction( ("msgSize_t","0"), "%s::deserialize" % name, "const uint8_t *", "size_t" )
        self.stubConstFunction( ("airware::airmail::IMessage *","(airware::airmail::IMessage *)g_%s_copy_arg0" % name), "%s::copy" % name, "void *" )
        self.stubFunction( ("void",), "%s::copyFrom" % name, "const airware::airmail::IMessage &" )
        self.stubConstFunction( ("size_t","0"), "%s::sizeOf" % name )

    def stubConstructor( self, name, argList, *inits ):
        self.cpp.write( "%s::%s( %s )" % (name, name, argList) )
        if len(inits) != 0:
            self.cpp.write( ":" )
        self.cpp.write("\n")
        for i in range( 0, len(inits) ):
            self.cpp.write( "    " + inits[i] )
            if i != len(inits)-1:
                self.cpp.write(",")
            self.cpp.write("\n")
        self.cpp.write( "{}\n\n" )

    def stubDestructor( self, name ):
        self.cpp.write( "%s::~%s( void )" % (name, name) )
        self.cpp.write("\n")
        self.cpp.write( "{}\n\n" )

    def stubSingleton( self, className, funcName ):
        self.cpp.write( "%s g_%s_singleton;\n" % (className, className ) )
        self.cpp.write( "%s *g_p%s_singleton = &g_%s_singleton;\n" % (className, className, className ) )
        self.cpp.write( "%s &%s::%s()\n" % (className, className, funcName) )
        self.cpp.write( "{\n" )
        self.cpp.write( "    return *g_p%s_singleton;\n" % className )
        self.cpp.write( "}\n\n" )
        self.resetCommands.append( "g_p%s_singleton = &g_%s_singleton;" % (className, className) )

    def stubFunction( self, retType, name, *args ):
        # Replace any special symbols in the name with _ in the stubName
        stubName = re.sub( "::", "_", name )
        self.stubOverload( retType, name, stubName, *args )

    def stubConstFunction( self, retType, name, *args ):
        # Replace any special symbols in the name with _ in the stubName
        stubName = re.sub( "::", "_", name )
        self.stubConstOverload( retType, name, stubName, *args )

    def stubOverload( self, retType, name, stubName, *args ):
        self.baseStubFunction( retType, name, stubName, False, *args )

    def stubConstOverload( self, retType, name, stubName, *args ):
        self.baseStubFunction( retType, name, stubName, True, *args )

    # Used to stub an overloaded function, where you need to specify a name of the function to overload and
    # a unique name for this stub. Also called generically by other forms of stub function creation
    def baseStubFunction( self, retType, name, stubName, const, *args ):

        # Define the calls value, and extern it
        defineCalls = "uint32_t g_%s_calls" % stubName
        self.cpp.write( defineCalls + " = 0;\n" )
        self.h.write( "extern " + defineCalls + ";\n" )
        self.resetCommands.append( "g_%s_calls = 0;" % stubName )

        # Define the hook, and extern it
        defineHook = "%s (*g_p%s_hook) ( " % (retType[0], stubName)
        if len(args) == 0:
            defineHook += "void"
        else:
            for i in range( 0, len(args)):
                defineHook +=  args[i]
                if i != ( len(args)-1 ):
                    defineHook += ", "
        defineHook += ")"
        self.cpp.write( defineHook + " = NULL;\n" )
        self.h.write( "extern " + defineHook + ";\n" )
        self.resetCommands.append( "g_p%s_hook = NULL;" % stubName )

        # Define the latest argument accessors and extern them
        argNames = []
        argGlobals = []
        argTypes = []
        for i in range( 0, len(args) ):
            fullType = args[i]
            if '&' not in fullType:  #Do not handle references since there is no good default for them
                nonConstType = ' '.join( fullType.replace( "const", "" ).split() ) # can't have consts
                argName = "arg%d" % i
                argGlobal = "g_%s_%s" % ( stubName, argName )
                defineArg = "%s %s" % ( nonConstType, argGlobal )
                self.cpp.write( defineArg + ";\n" )
                self.h.write( "extern " + defineArg + ";\n" )
                argNames.append( argName )
                argGlobals.append( argGlobal )
                argTypes.append( nonConstType )

        # Define the return value, and extern it
        if retType[0] != "void":
            defineRet = "%s g_%s_return" % (' '.join( retType[0].split() ), stubName) # Generate return twiddler with proper whitespacing
            self.cpp.write( defineRet + " = %s;\n" % retType[1] )
            self.h.write( "extern " + defineRet + ";\n" )
            if '&' not in retType[0]: #Can't change references (therefore no need to reset them either)
                self.resetCommands.append( "g_%s_return = %s;" % ( stubName, retType[1] ) )

        # Add newline after header externs
        self.h.write( "\n" )
        # Define the stub function
        self.cpp.write( "%s %s(" % (retType[0], name) )
        if len(args) == 0:
            self.cpp.write( "void )" )
        else:
            for i in range( 0, len(args) ):
                self.cpp.write( "%s arg%d" % ( args[i], i ) )
                if i != ( len(args)-1 ):
                    self.cpp.write( "," )
            self.cpp.write( ")" )
        if const:
            self.cpp.write( " const" )
        self.cpp.write( "\n" )
        self.cpp.write( "{\n" )
        self.cpp.write( "    g_%s_calls++;\n" % stubName )
        for i in range( 0, len( argNames ) ):
            self.cpp.write( "    %s = (%s)( %s );\n" % ( argGlobals[i], argTypes[i], argNames[i] ) ) # cannot use const_cast since types might be the same
        self.cpp.write( "    if( g_p%s_hook != NULL ) {\n" % stubName )
        self.cpp.write( "        " )
        if retType[0] != "void":
            self.cpp.write( "return " )
        self.cpp.write( "g_p%s_hook(" % stubName )
        if len(args) != 0:
            for i in range( 0, len(args)):
                self.cpp.write( "arg%d" % i )
                if i != ( len(args)-1 ):
                    self.cpp.write( ", " )
        self.cpp.write( ");\n" )
        self.cpp.write( "    }\n" )
        if retType[0] != "void":
            self.cpp.write( "    return g_%s_return;\n" % stubName )
        self.cpp.write( "}\n" )
        self.cpp.write( "\n" )

    # Finish and close files
    def __del__(self):
        # Write footer(s)
        if( self.externCed ):
            self.cpp.write( "#ifdef __cplusplus\n" )
            self.cpp.write( "} /*extern \"C\"*/\n" )
            self.cpp.write( "#endif\n\n" )
            self.h.write( "#ifdef __cplusplus\n" )
            self.h.write( "} /*extern \"C\"*/\n" )
            self.h.write( "#endif\n\n" )

        self.h.write( "\n" )
        self.h.write( "void reset_%s_stubs( void );\n" % self.m_module  )

        self.cpp.write( "\n" )
        self.cpp.write( "void reset_%s_stubs( void )" % self.m_module  )
        self.cpp.write( "{\n" )
        for line in self.resetCommands:
            self.cpp.write( "    %s\n" % line )
        self.cpp.write( "}\n" )

        self.h.write( "\n#endif /*STUB_HEADER_%s*/\n" % self.m_module )

        #Close files
        self.cpp.close()
        self.h.close()
