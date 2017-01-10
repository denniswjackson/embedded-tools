# Only include this file once
ifndef COMPONENT_NAME

COMPONENT_NAME = "apollo"

# Read the repo version
VERSION_FILE := $(BASE)/VERSION
VERSION_STR := $(shell cat ${VERSION_FILE})
VERSION_SPACE_DELIMITED := $(subst ., ,${VERSION_STR})

# Pull apart the pieces for those who need them
VERSION_MAJOR = $(word 1, $(VERSION_SPACE_DELIMITED))
VERSION_MINOR = $(word 2, $(VERSION_SPACE_DELIMITED))
VERSION_PATCH = $(word 3, $(VERSION_SPACE_DELIMITED))

ifndef BUILD_NUMBER
BUILD_NUMBER  = 0
endif

ifndef BUILD_VCS_NUMBER
# local build
GIT_HASH := $(shell git log -1 --format=%h)
else
# teamcity
GIT_HASH := $(shell echo $${BUILD_VCS_NUMBER:0:7})
endif

# Redirecting this macro to a file generates version.cpp for this repo
define VERSION_CPP
#include "common/version.h"
const uint8_t airware::commonSat::VERSION_MAJOR = $(VERSION_MAJOR);
const uint8_t airware::commonSat::VERSION_MINOR = $(VERSION_MINOR);
const uint8_t airware::commonSat::VERSION_PATCH = $(VERSION_PATCH);
const uint16_t airware::commonSat::BUILD_NUMBER = $(BUILD_NUMBER);
const char* airware::commonSat::COMPONENT_NAME = $(COMPONENT_NAME);
const char* airware::commonSat::GIT_HASH = "$(GIT_HASH)";
endef
export VERSION_CPP


printVersion:
	@echo "Component:       $(COMPONENT_NAME)"
	@echo "String:          $(VERSION_STR)"
	@echo "Space delimited: $(VERSION_SPACE_DELIMITED)"
	@echo "Reconstructed:   $(VERSION_MAJOR).$(VERSION_MINOR).$(VERSION_PATCH).$(BUILD_NUMBER)"
	@echo "Git Hash:        $(GIT_HASH)"

endif
