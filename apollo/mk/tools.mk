# Output directory. Place all .a, and .exe files here
OUTPUT = $(BASE)/output

# Use this as an order-only prerequisite to make sure the folder exists
# See http://www.gnu.org/software/make/manual/html_node/Prerequisite-Types.html
$(OUTPUT):
	mkdir -p $(OUTPUT)

include $(BASE)/mk/debug.mk

#-----------------------------------------------
#                  ARM Compiler
#-----------------------------------------------
# look for options for Keil installations (for
# teamcity compatibility etc.)
KEIL_BASE = C:/Keil
ifeq ("$(wildcard $(KEIL_BASE))","")
    KEIL_BASE = D:/Keil
endif

ARM_CXX = "$(KEIL_BASE)/ARM/ARMCC/bin/armcc.exe"
ARM_CC = "$(KEIL_BASE)/ARM/ARMCC/bin/armcc.exe"
ARM_AS = "$(KEIL_BASE)/ARM/ARMCC/bin/armasm.exe"
ARM_LD = "$(KEIL_BASE)/ARM/ARMCC/bin/armlink.exe"
ARM_FROMELF = "$(KEIL_BASE)/ARM/ARMCC/bin/fromelf.exe"

# common ARM flags
ARM_CXXFLAGS = --diag_error=warning --cpp --cpu Cortex-M4.fp --apcs=interwork --split_sections -g -O0
ARM_CFLAGS = --diag_error=warning --cpu Cortex-M4.fp --apcs=interwork --split_sections -g -O0
ARM_ASFLAGS = --cpu Cortex-M4.fp --apcs=interwork -g
ARM_LDFLAGS = --cpu Cortex-M4.fp --diag_suppress 6314,6329 --strict --summary_stderr --info summarysizes --map --xref --callgraph --symbols --info sizes --info totals --info unused --info veneers

# These all need to be available in recursive make calls
export ARM_CXX
export ARM_CC
export ARM_AS
export ARM_LD
export ARM_FROMELF
export ARM_CXXFLAGS
export ARM_CFLAGS
export ARM_ASFLAGS
export ARM_LDFLAGS

#-----------------------------------------------
#                  Adev  }:-)~>
#-----------------------------------------------

# Set up airware tools using the adev tool - this must be run as administrator
# note: adev setup has to check with a server every time to make sure it is up to
# date, which takes time, and requires a VPN, so use it sparingly.
.PHONY: setup
setup:
	adev setup analyze x86_64-cygwin-gcc
	adev setup package x86_64-cygwin-gcc
	adev setup package arm-uios-keil-m4
	@echo "WiX is required for building the sim installer.  See the readme.md for details."

#-----------------------------------------------
#        Global definitions
#-----------------------------------------------

# python tools
PYTHON_TOOLS_DIR = c:/Python27/Scripts

# Tool definitions
RUN_MAP_FILE_STATS = $(PYTHON_TOOLS_DIR)/mapFileStats.py
RUN_FORMAT_CODE = astyle $(FORMAT_CODE_OPTIONS)

FORMAT_CODE_OPTIONS = --options=$(BASE)/.astylerc

COMPRESS_CMD = tar -cvzf

#-----------------------------------------------
#       Continuous Integration Server 
#-----------------------------------------------

# Verifies the input file or directory exists and publishes it if it does
# params:
#   1. path to file to post
# "strip" is required for the name in case the caller inadvertently adds 
# whitespace on either end of the string
define publish-artifact
	@test -f $(1) || test -d $(1) || { echo "Error $(1) does not exist"; exit 1; }
	@echo "##teamcity[publishArtifacts '$(strip $(1))']"
endef
