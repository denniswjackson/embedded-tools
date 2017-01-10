# LDRA configuration -- use the same mode for all components
ANALYZE_MODE := RUNTIME
ANALYZE_EXE  := c:/LDRA_Toolsuite/Contestbed.exe
RUN_ANALYZE_STATS = python $(PYTHON_TOOLS_DIR)/ldra_parser.py

# Limit the number of files included in the set to this amount at once. All files
# list are added before the analysis is run. This was added for the Flight Core build.
ANALYZE_MAX_FILE_ARGS := 20

# Parameters: 
#   1. LDRA analyze set name
#   2. project *_LDRA_INCLUDE_PATHS (this should not include paths under `deps/` otherwise analysis will take significantly longer)
#   3. project *_ANALYZE_SOURCE
#   4. project *_ANALYZE_OUTPUT
#   5. project *_ANALYZE_DEFINES
#   6. project *_ANALYZE_MAND_VIOLATION_THRESHOLD
#   7. project *_ANALYZE_COND_VIOLATION_THRESHOLD
define run-ldra =
    @echo "LDRA Analyze parameters"
    @echo " - Set name                        = $(1)"
    @echo " - Include Paths                   = $(2)"
    @echo " - Source files                    = $(3)"
    @echo " - Output folder                   = $(4)"
    @echo " - Preprocessor defs               = $(5)"
    @echo " - Mandatory Violation threshold   = $(6)"
    @echo " - Conditional Violation threshold = $(7)"
    
    $(eval SYSPP_FILE := `cygpath -m $(abspath $(5))`)
    @echo " - SYSPP_FILE                      = $(SYSPP_FILE)"
    $(eval LDRA_INPUT_FILE := $(OUTPUT)/$(1)_include.txt)
    @echo " - LDRA_INPUT_FILE                 = $(LDRA_INPUT_FILE)"
    @echo

    @# sort the input list to remove duplicates
    $(eval SORTED_SRC := $(sort $(3)))

    @# create a temporary input file for LDRA
    $(eval LDRA_INPUT_FILE := $(shell mkdir -p $(OUTPUT); mktemp -p $(OUTPUT)))
    
    @echo "Removing data from the previous run"
    $(ANALYZE_EXE) /delete_set=$(1) /1q

    @echo "Configuring files for set $(1)"
    $(ANALYZE_EXE) $(1) /create_set=group /1q
    @echo "0 LDRA static analysis include file path configuration" > $(LDRA_INPUT_FILE)
    @echo  $(foreach incPath, $(2), "1 `cygpath -w $(abspath $(subst -I, ,$(incPath))) && echo ' '`") >> $(LDRA_INPUT_FILE)
    @$(call max_args,$(ANALYZE_EXE) $(1) /1q,$(ANALYZE_MAX_FILE_ARGS),$(foreach srcFile, $(SORTED_SRC),/add_set_file=$(shell cygpath -m $(abspath $(srcFile)))))

    @echo "Running static analysis of C++ files using $(ANALYZE_MODE) rules"
    @$(ANALYZE_EXE) $(1) /CPPquality_model=$(ANALYZE_MODE) /sysearch=$(shell cygpath -m $(abspath $(LDRA_INPUT_FILE))) /112a34q /publish_to_dir=$(shell cygpath -m $(abspath $(4))) /html_index_template=FULL /publish_rep_type=HTML /sysppvar=$(SYSPP_FILE)
    
    @echo "Generating results for TeamCity"
    $(RUN_ANALYZE_STATS) --mand_violation_thresh $(6) --cond_violation_thresh $(7) $(4)
    
    # clean up
    rm -f $(LDRA_INPUT_FILE)
    
    $(call publish-artifact,$(4))
endef

# Functions to split long lists into smaller components to send to command line tools
# Source: https://blog.melski.net/2012/01/03/makefile-hacks-automatically-split-long-command-lines/
define max_args
  $(eval _args:=)
  $(foreach obj,$3,$(eval _args+=$(obj))$(if $(word $2,$(_args)),$1$(_args)$(EOL)$(eval _args:=)))
  $(if $(_args),$1$(_args))
endef
define EOL


endef
