## This module contains functions for building MSVC projects and checking their line coverage

MSVC_BUILD = $(BASE)/buildScripts/msvc

MS_BUILD_CMD        = /cygdrive/c/Program\ Files\ \(x86\)/MSBuild/14.0/Bin/MSBuild.exe
MS_GET_COVERAGE_CMD = /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 14.0/Team\ Tools/Dynamic\ Code\ Coverage\ Tools/CodeCoverage.exe

# Arguments to pass to the unit test when generating code coverage
CPPUTEST_ARGS = -ojunit

# Preprocessor definitions for MSVC builds
MSVC_DEFINES = _WINDOWS STM32F427_437xx WIN32_LEAN_AND_MEAN NOMINMAX _CRT_SECURE_NO_WARNINGS
MSVC_UT_DEFINES = CPPUTEST_MEM_LEAK_DETECTION_DISABLED CPPUTEST_STD_CPP_LIB_DISABLED AW_UNIT_TEST=1

# This command creates a target to build msvc project files
# Arguments:
#   $(1) = output project path and name (without the .vcxproj extension)
#   $(2) = list of all makefiles which define source lists
#   $(3) = list of all include paths
#   $(4) = list of all preprocessor definitions
#   $(5) = list of all source/lib groups in format --group "Name1 source list" --group "Name2 source list..."
define MS_PROJ_TARGET
$(1).out.sln: $(BASE)/Makefile $(MK_DIR)/deps.mk $(2) $(MSVC_BUILD)/Template.vcxproj $(MSVC_BUILD)/Template.vcxproj.filters $(MSVC_BUILD)/makeMsvcProj.py | $(OUTPUT)
	mkdir -p $(dir $(1))
	python $(MSVC_BUILD)/makeMsvcProj.py --template $(MSVC_BUILD)/Template --output $(1) -I "$(3)" -D "$(4)" $(5)
	cp $(MSVC_BUILD)/prebuild.bat $(1).out.bat
	sed -i.bkp 's/Template/$(notdir $(1))/g' $(1).out.bat
	cp $(MSVC_BUILD)/Template.sln $(1).out.sln
	sed -i.bkp 's/Template/$(notdir $(1)).out/g' $(1).out.sln
endef

# This command creates a target to build an debug executable from an MSVC solution
# Arguments:
#   $(1) = output executable path and name
#   $(2) = path and name of solution, without the .sln extension, assumes sln proj and filters all share the same name
#   $(3) = list of all source files to add as dependencies to the target
#
# Also create a $(2).deps target that can be used to execute pre-build steps. Give his a convenient name: name_DEPS that
# can be called from a from visual studio pre-build step
#
# Note: The .exe is always created in the folder "../build/x86D" relative to the solution file. This step copies the
#       executable to the output folder.  No files are published to the CI server from this set of targets.
#
# Known Issue: Building with -j8 flag set will raise warning: "jobserver unavailable: using j1" This is because MSBUILD
#    invokes make name_DEPS, from within the context of a multi-core build. Adding '+' to the MS_BUILD_CMD does not seem
#    to help. In any case, this shouldn't be an issue, since, if this command is invoked from the command line, the deps
#    have already been built, and the pre-build step will see this and do nothing.
define MS_EXE_TARGET
$(notdir $(2))_DEPS: $(2).deps
$(2).deps: $(DEPS)/x86DDepsPresent $(2).out.sln $(3)
	touch $(2).deps
$(1): $(2).deps | $(OUTPUT)
	$(MS_BUILD_CMD) /maxcpucount /p:Configuration="Debug" $(2).out.sln
	cp $(dir $(2))../build/x86D/$(notdir $(2)).exe $(1)
endef

# This command creates a target to build a release executable from an MSVC solution
#   same notes as for MS_EXE_TARGET
#
# Note 1: the project will be built using the solution's release configuration
#
# Note 2: The .exe is always created in the folder "../build/x86" relative to the solution file. This step copies the
#         executable to the output folder.   No files are published to the CI server from this set of targets;
#         they are bundled up with MSI files.
#
# Note 3: Debug deps are downloaded as well. This is because the project probably needs headers and/or source from
#         projects for which there is not release build
define MS_EXE_RELEASE
$(notdir $(2))_DEPS: $(2).deps
$(2).deps: $(DEPS)/x86DepsPresent $(DEPS)/x86DDepsPresent $(2).out.sln $(3)
	touch $(2).deps
$(1): $(2).deps | $(OUTPUT)
	$(MS_BUILD_CMD) /maxcpucount /p:Configuration="Release" $(2).out.sln
	cp $(dir $(2))../build/x86/$(notdir $(2)).exe $(1)
endef

# This command creates a coverage report of an MS build
# Arguments:
#   $(1) = path and name of xml coverage file to output
#   $(2) = path and name of unit test executable built with profiling information
#   $(3) = Line coverage threshold
#   Note: the old coverage report must be deleted or generation of the new one may fail
define MS_COVERAGE_TARGET
$(1).xml: $(2) $(MSVC_BUILD)/CodeCoverage.config
	rm -f $(1).coverage
	rm -f $(1).xml
	$(MS_GET_COVERAGE_CMD) collect /config:$(MSVC_BUILD)/CodeCoverage.config /output:$(1).coverage $(2) $(CPPUTEST_ARGS)
	$(MS_GET_COVERAGE_CMD) analyze /output:$(1).xml $(1).coverage
	python $(MSVC_BUILD)/checkMsvcCoverage.py --input $(1).xml --threshold $(3)
	@echo "##teamcity[importData type='junit' path='$(BASE)/cpputest_*.xml']"
	$(eval UT_ARTIFACT := $(basename $(2)).tar.gz)
	$(COMPRESS_CMD) $(UT_ARTIFACT) $(1).coverage $(1).xml $(2)
	$(call publish-artifact,$(UT_ARTIFACT))
endef

# This command runs a test without gathering coverage
# Arguments:
#   $(1) = path and name of unit test executable
#   This will create a target named $(1)_runTest
define RUN_TEST_TARGET
$(1)_runTest: $(1)
	$(1) $(CPPUTEST_ARGS)
	$(call publish-artifact,$(1))
endef
