# The stub factory
The stub factory is a utility which generates stub source and header files in the standard Airware form. The stub source is built into unit tests. If access to the stub hooks or twiddlers is needed, the stub header may be also be included in the unit test. At no time should these files or headers be included in production code

## Generating stubs
To generate stubs for a module X, add a `stub_X.py` to the stubFactory folder, and add `stub_x.cpp` and `stub_x.h` to the list of stubs in the stub factory Makefile.

## Building stubs into your test
Add the stub source from `bin/stubFactory/build` to your project's Makefile. Be sure to build object code in your project's own build directory so that it does not conflict with other projects sharing the same stub code.

If you want to utilize the stub includes, you also need to add `$(BASE)/bin/stubFactory/build` to the include path, and add a dependency on `$(STUB_SOURCES)` to your test file builds. The explicit dependency makes sure that make auto-generates the headers your source files will need. The Makefile can't figure this out automatically, because the .d files cannot be build until the header is generated.

## Using stubs

### Hooks
If the auto-generated stub is not sufficient for your test's needs, you can set the `g_p[name]_hook` global to point to a custom stub.
Setting the hook to NULL will return the stub to its default behaviour.

### Returns
To cause the stub to return a value other than the default, set the `g_[name]_returns` global to the new return value. This should be reset after each test

### Number of calls
The `g_[name]_calls` 32 bit counter tracks the number of times the stub has been called. This should be reset after each test

### Arguments
The `g_[name]_arg[n]` global contains the most recent argument passed to the stub. This value is only valid if `g_[name]_calls` > 0 (otherwise stub factory would need to infer a default for each type). Accessors are not generated for reference arguments, since references cannot be changed once set. Accessors are also non-const, the stub casts away the constness of the argument so it can make a copy of it.

### Reset
For each set of stubs a `reset_[name]_stubs()` function is generated. Call this from your test case's teardown function to reset all hooks to NULL, set all `g_[name]_calls` counters back to 0, and set all return values back to the default

## stub_x.py format

The module _class::method_

Every file should start with

    import sys
    from genStubs import *
    stub = Stubs( "name", sys.argv[1], sys.argv[2] )

and "name" should always match the file name. For example, `stub_uios.py` should use "uios" as the name. This sets up the "stub" object which you will use in all subsequent calls.

* `stub.include( "header.h" )` adds a #include to the stubs. These are needed to declare the types needed by the stubs

* `stub.useNamespace( "[namespace]" )` adds a "using namespace" directive so you don't need to include fully qualified names in the stub files

* `stub.stubFunction( ("void",), "[Name]" )` adds a stub for a function named [Name] with no return and no params

* `stub.stubFunction( ("[type]", "[defaultReturn]"), "[Name]", "[Arg type 1]", "[Arg type 2]", ... )`
adds a stub for a function with a return type and arguments.

If you are stubbing an overloaded function, then use
`stub.stubOverload( ("[type]", "[defaultReturn]"), "[Name]", "[uniqueNameForHooks]", args... )`

To stub a `const` function, use `stub.stubConstFunction` and `stub.stubConstOverload`

Note that in all these cases, [Name] can be a method name e.g. "Class::Method"

If you need to `extern "C"{` your stub, then use
`stub.externC()` Everything after this line will be given C linkage, and the extern will be automatically closed at the end of the file

If the standard stub utilities don't cover something that use need to add, then just add a source line to the stub file with:
`stub.addLine( "[This line goes directly into stub source];" )` This is useful for instantiating a global variable in the module being stubbed, for example.


## Standard Airware stub format
Stubbing the function
`ret CClass::Name( args... )` creates stub code:

    uint32_t g_CClass_Name_calls = 0;
    ret g_CClass_Name_return = false;
    ret (*g_pCClass_Name_hook) ( args... ) = NULL;
	arg0Type g_CClass_Name_arg0;
	...
	argnType g_CClass_Name_argn;
    ret CClass::Name( args... )
    {
	    g_CClass_Name_arg0 = (arg0Type)arg0;
	    ...
	    g_CClass_Name_argn = (argnType)argn;
	    g_CClass_Name_calls++
        if( g_pCClass_Name_hook != NULL ) {
            return g_pCClass_Name_hook( args... );
        }
        return g_CClass_Name__return;
    }

## Examples

### stub_common.py

    stub.stubFunction( ("bool","false"), "CSatCore::paramLibInit", "int8_t&", "bool&", "bool&" )

### build/stub_common.cpp

    #define private public
    #define protected public
    #include "common/CSatCore.h"
    #undef private
    #undef protected
    
    using namespace airware::commonSat;
    
    bool g_CSatCore_paramLibInit_return = false;
    bool (*g_pCSatCore_paramLibInit_hook) ( int8_t&, bool&, bool&) = NULL;
    bool CSatCore::paramLibInit(int8_t& arg0,bool& arg1,bool& arg2)
    {
        if( g_pCSatCore_paramLibInit_hook != NULL ) {
            return g_pCSatCore_paramLibInit_hook(arg0, arg1, arg2);
        }
        return g_CSatCore_paramLibInit_return;
    }

### build/stub_common.h

    extern bool g_CSatCore_isParamLibInitialized_return;
    extern bool (*g_pCSatCore_isParamLibInitialized_hook) ( void);