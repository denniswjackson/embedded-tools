## This module contains functions for building Keil uVision projects
include $(MK_DIR)/awx.mk

KEIL_SCRIPTS_DIR = $(BASE)/buildScripts/keil

KEIL_BUILD_CMD = $(KEIL_BASE)/UV4/UV4.exe

CREATE_FILE_DESCRIPTOR_PY = $(PYTHON_TOOLS_DIR)/createFileDescriptor.py

# Test Automation tooling. For details, see 
# http://confluence/display/TE/Build+Specification+Names+and+Versions
CREATE_BUILD_SPEC_PY      = $(PYTHON_TOOLS_DIR)/createBuildSpec.py
MAKE_HEADER_PY = $(KEIL_SCRIPTS_DIR)/makeImageHeader.py
BUILD_SPEC_NAME = "factory"
BUILD_SPEC_VERSION = "2.0"

# Note: the job server is not supported on all architectures, most notably many
# versions of Windows which we actually use to build. When this is the case,
# make will not allow propagation of the -jN command line argument to recursive
# sub-processes since the child processes don't know how many make instances
# are already running. We introduce the SUB_JOBS make variable to work around
# this. To enable highly parallelized builds do "make SUB_JOBS=N" where "N"
# is the number of logical cores available on your system.
ifeq ("$(SUB_JOBS)","")
    SUB_JOBS = 1
endif

# Commonly used sets of preprocessor definitions

# This command creates a target to build keil uVision project files
# Arguments:
#   $(1) = template project file
#   $(2) = output project file
#   $(3) = output hex file
#   $(4) = build directory
#   $(5) = list of all makefiles which define source lists
#   $(6) = list of all include paths
#   $(7) = list of all preprocessor definitions
#   $(8) = list of all assembler definitions
#   $(9) = scatter file
#   $(10) = list of all source/lib groups in format --group "Name1 source list" --group "Name2 source list..."
define UV_PROJ_TARGET
$(2) $(basename $(2)).mk: $(BASE)/Makefile $(MK_DIR)/deps.mk $(COMMON_DIR)/Makefile $(1) $(5) $(KEIL_SCRIPTS_DIR)/makeKeilProj.py
	mkdir -p $(dir $(2))
	mkdir -p $(dir $(3))
	mkdir -p $(4)
	python $(KEIL_SCRIPTS_DIR)/makeKeilProj.py --template $(1) --output $(2) --target $(3) --build $(4) -I "$(6)" -D "$(7)" --asm "$(8)" --scatter $(9) $(10)
	cp $(KEIL_SCRIPTS_DIR)/prebuild.bat $(dir $(2))prebuild.out.bat
	sed -i.bkp 's/Template/$(notdir $(2))/g' $(dir $(2))prebuild.out.bat
endef

# This command creates a target to build a hex file (and its file descriptor) from a keil project
# including the standard boot header for applications
#
# Arguments:
#   $(1) = output executable hex
#   $(2) = keil project to build
#   $(3) = build directory
#   $(4) = list of all source files to add as dependencies to the target
#   $(5) = The sector for which the hex is destined (createFileDescriptor.py "fileType")
#   $(6) = Variant of the application to record in file descriptor (createFileDescriptor.py "fileVariant")
#   $(7) = The hardware compatibility csv file
#   $(8) = the architecture string
#   $(9) = optionally, additional arguments to RUN_MAP_FILE_STATS

# Also create a $(2).deps target that can be used to execute pre-build steps
define HEX_TARGET
$(notdir $(2))_DEPS: $(2).deps
$(2).deps: $(DEPS)/armDepsPresent $(2) $(4)
	touch $(2).deps

$(1): $(2).deps $(2) $(basename $(2)).mk
	$(MAKE) -j$$(SUB_JOBS) -f $(basename $(2)).mk $(3)/$(basename $(notdir $(1))).axf
	$(ARM_FROMELF) $(3)/$(basename $(notdir $(1))).axf --i32combined --output $(3)/$(notdir $(1))
	# note that BUILD_NUMBER gets defined to 0 if this isn't a teamcity build
	python $(MAKE_HEADER_PY) $(3)/$(notdir $(1)) -v $(VERSION_STR) -s $(5) -a $(8) -b $(BUILD_NUMBER) -o $(1)
	cp $(3)/$(basename $(notdir $(1))).map $(dir $(1))
	python $(RUN_MAP_FILE_STATS) $(subst .hex,.map,$(1)) $(9)

$(1).json: $(1)
	python $(CREATE_FILE_DESCRIPTOR_PY) $(1) $(5) $(6) $(VERSION_STR) $(dir $(2))../$(strip $(7))
	python $(CREATE_BUILD_SPEC_PY) -o $(dir $(1)) $(BUILD_SPEC_NAME) $(BUILD_SPEC_VERSION)
endef

# This command creates a target to build a hex file (and its file descriptor) from a keil project
# (without a header)
#
# Arguments:
#   $(1) = output executable hex
#   $(2) = keil project to build
#   $(3) = build directory
#   $(4) = list of all source files to add as dependencies to the target
#   $(5) = The sector for which the hex is destined (createFileDescriptor.py "fileType")
#   $(6) = Variant of the application to record in file descriptor (createFileDescriptor.py "fileVariant")
#   $(7) = The hardware compatibility csv file
#   $(8) = optionally, additional arguments to RUN_MAP_FILE_STATS

# Also create a $(2).deps target that can be used to execute pre-build steps
define HEX_TARGET_NO_HEADER
$(notdir $(2))_DEPS: $(2).deps
$(2).deps: $(DEPS)/armDepsPresent $(2) $(4)
	touch $(2).deps

$(1): $(2).deps $(2) $(basename $(2)).mk
	$(MAKE) -j$$(SUB_JOBS) -f $(basename $(2)).mk $(3)/$(basename $(notdir $(1))).axf
	$(ARM_FROMELF) $(3)/$(basename $(notdir $(1))).axf --i32combined --output $(1)
	cp $(3)/$(basename $(notdir $(1))).map $(dir $(1))
	python $(RUN_MAP_FILE_STATS) $(subst .hex,.map,$(1)) $(8)

$(1).json: $(1)
	python $(CREATE_FILE_DESCRIPTOR_PY) $(1) $(5) $(6) $(VERSION_STR) $(dir $(2))../$(strip $(7))
	python $(CREATE_BUILD_SPEC_PY) -o $(dir $(1)) $(BUILD_SPEC_NAME) $(BUILD_SPEC_VERSION)
endef

# This script generates an awx (and its descriptor) from a hex
# Arguments:
#   $(1) = output awx
#   $(2) = input hex
#   $(3) = PID
#   $(4) = The sector for which the hex is destined (createFileDescriptor.py "fileType")
#   $(5) = Variant of the application to record in file descriptor (createFileDescriptor.py "fileVariant")
#   $(6) = A file indicating which hardware this awx is compatible with
define AWX_TARGET
$(1): $(2)
	mkdir -p $(dir $(1))
	python $(RUNAWXTOOL) $(AWXTOOL_ARGS) --imageType $(4) --targetProductId $(3) -i $(2) -o $(1)

$(1).json: $(1)
	python $(CREATE_FILE_DESCRIPTOR_PY) $(1) $(4) $(5) $(VERSION_STR) $(6) dev
endef
