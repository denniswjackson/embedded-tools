# Moneta parameter configuration -- use the same mode for all components
PARAMS_PY = $(MONETA_DIR)/py/moneta/monetify.py
GLOBAL_MANIFEST_FILE = $(COMMON_DIR)/params/globalManifest.json
VERSION_FILE = $(BASE)/VERSION

ifeq ("$(CREATE_FILE_DESCRIPTOR_PY)","")
CREATE_FILE_DESCRIPTOR_PY = $(PYTHON_TOOLS_DIR)/createFileDescriptor.py
endif


# params:
#   1. Name of the application (e.g. act04p)
#   2. Path to the base of the application
#   3. Desired output path for the param meta table C++ file
#   4. Desired output path for the numeric IDs header file
#   5. Path to where output artifacts (e.g. hex files) should go
define BUILD_PARAMS
$(eval PARAM_MANIFEST := $(2)/params/$(1)Params.json)
$(eval APP_WORKING_SET := $(5)/$(1)WorkingSet.hex)
$(3) $(4): $(PARAM_MANIFEST) $(GLOBAL_MANIFEST_FILE) $(wildcard $(MONETA_DIR)/py/moneta/*.py)
	mkdir -p $(dir $(3))
	mkdir -p $(dir $(4))
	python $(PARAMS_PY) -w $(APP_WORKING_SET) -a $(PARAM_MANIFEST) -m $(3) -n $(4) -g $(GLOBAL_MANIFEST_FILE) -V $(VERSION_FILE) -A $(BASE)/keys/e01FwDv -R $(BASE)/keys/s01FwDv
endef

# params for pkid:
#   1. Path to the base of the application
#   2. Desired output path for the param meta table C++ file
#   3. Desired output path for the numeric IDs header file
#   4. Path to where output artifacts (e.g. hex files) should go
define BUILD_PARAMS_FOR_PKID
$(eval PKID_GLOBAL_MANIFEST_FILE := $(1)/params/globalManifest.json)
$(eval PARAM_MANIFEST := $(1)/params/pkidParams.json)
$(eval APP_WORKING_SET := $(4)/pkidWorkingSet.hex)
$(2) $(3): $(PARAM_MANIFEST) $(PKID_GLOBAL_MANIFEST_FILE) $(wildcard $(MONETA_DIR)/py/moneta/*.py)
	mkdir -p $(dir $(2))
	mkdir -p $(dir $(3))
	python $(PARAMS_PY) -w $(APP_WORKING_SET) -a $(PARAM_MANIFEST) -m $(2) -n $(3) -g $(PKID_GLOBAL_MANIFEST_FILE) -V $(VERSION_FILE) -R $(BASE)/keys/s01FwDv
endef

# params for simulator:
#   1. Path to the base of the application
#   2. Path to where output working set should go
# Note: The working set BIN files are built into the release MSI and are not published on TeamCity
define BUILD_PARAMS_FOR_SIM
$(2)/%.wset.bin: $(1)/params/%.json $(GLOBAL_MANIFEST_FILE) $(wildcard $(MONETA_DIR)/py/moneta/*.py)
	mkdir -p $(2)
	python $(PARAMS_PY) -w $$@ -a $$< -g $(GLOBAL_MANIFEST_FILE) -V $(VERSION_FILE) -A $(BASE)/keys/e01FwDv -R $(BASE)/keys/s01FwDv
endef

# params for Hilsim
#   1. Path to the base of the application
#   2. Path to where output working set should go
#   3. Path to the hardware compatibility csv file
define BUILD_PARAMS_FOR_HILSIM
$(2)/%FWHilsim.wset.hex: $(1)/params/%FWHilsim.json $(GLOBAL_MANIFEST_FILE) $(wildcard $(MONETA_DIR)/py/moneta/*.py)
	mkdir -p $(2)
	python $(PARAMS_PY) -w $$@ -a $$< -g $(GLOBAL_MANIFEST_FILE) -V $(VERSION_FILE) -A $(BASE)/keys/e01FwDv -R $(BASE)/keys/s01FwDv
	python $(CREATE_FILE_DESCRIPTOR_PY) $$@ ps1 hilsim $(VERSION_STR) $(3)
endef

