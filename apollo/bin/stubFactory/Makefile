# If this module has not been included from another, import Apollo Makefile
ifndef BASE
	include ../../Makefile
else

STUBS_DIR = $(BASE)/bin/stubFactory
STUBS_BUILD = $(STUBS_DIR)/build


#-----------------------------------------------
#             Auto-generate Source
#-----------------------------------------------
STUB_HEADERS =  $(STUBS_BUILD)/stub_CMs5611.h \
                $(STUBS_BUILD)/stub_admBsp.h \
                $(STUBS_BUILD)/stub_airBoot.h \
                $(STUBS_BUILD)/stub_airmail.h \
                $(STUBS_BUILD)/stub_common.h \
                $(STUBS_BUILD)/stub_control.h \
                $(STUBS_BUILD)/stub_egbBsp.h \
                $(STUBS_BUILD)/stub_flightCore.h \
                $(STUBS_BUILD)/stub_flightCoreBsp.h \
                $(STUBS_BUILD)/stub_hades.h \
                $(STUBS_BUILD)/stub_jsbsim.h \
                $(STUBS_BUILD)/stub_jtagFuse.h \
                $(STUBS_BUILD)/stub_keyStash.h \
                $(STUBS_BUILD)/stub_logger.h \
                $(STUBS_BUILD)/stub_micrium.h \
                $(STUBS_BUILD)/stub_moneta.h \
                $(STUBS_BUILD)/stub_navigation.h \
                $(STUBS_BUILD)/stub_neom8.h \
                $(STUBS_BUILD)/stub_paramLib.h \
                $(STUBS_BUILD)/stub_scap.h \
                $(STUBS_BUILD)/stub_systemMessages.h \
                $(STUBS_BUILD)/stub_ubx.h \
                $(STUBS_BUILD)/stub_uios.h

STUB_SOURCES =  $(STUBS_BUILD)/stub_CMs5611.cpp \
                $(STUBS_BUILD)/stub_admBsp.cpp \
                $(STUBS_BUILD)/stub_airBoot.cpp \
                $(STUBS_BUILD)/stub_airmail.cpp \
                $(STUBS_BUILD)/stub_common.cpp \
                $(STUBS_BUILD)/stub_control.cpp \
                $(STUBS_BUILD)/stub_egbBsp.cpp \
                $(STUBS_BUILD)/stub_flightCore.cpp \
                $(STUBS_BUILD)/stub_flightCoreBsp.cpp \
                $(STUBS_BUILD)/stub_hades.cpp \
                $(STUBS_BUILD)/stub_jsbsim.cpp \
                $(STUBS_BUILD)/stub_jtagFuse.cpp \
                $(STUBS_BUILD)/stub_keyStash.cpp \
                $(STUBS_BUILD)/stub_logger.cpp \
                $(STUBS_BUILD)/stub_micrium.cpp \
                $(STUBS_BUILD)/stub_moneta.cpp \
                $(STUBS_BUILD)/stub_navigation.cpp \
                $(STUBS_BUILD)/stub_neom8.cpp \
                $(STUBS_BUILD)/stub_paramLib.cpp \
                $(STUBS_BUILD)/stub_scap.cpp \
                $(STUBS_BUILD)/stub_systemMessages.cpp \
                $(STUBS_BUILD)/stub_ubx.cpp \
                $(STUBS_BUILD)/stub_uios.cpp

#Auto-gen stub sources
$(STUBS_BUILD)/stub_%.cpp: $(STUBS_DIR)/stub_%.py $(STUBS_DIR)/genStubs.py
	mkdir -p $(STUBS_BUILD)
	python $< $(STUBS_BUILD) $(STUBS_BUILD)

# This tells make that stub_%.h is generated at the same time stub_%.cpp is. Don't let it generate both independently
# or it will do them in parallel, and the files from the 2 processes may overwrite each other when building in parallel
$(STUBS_BUILD)/stub_%.h: $(STUBS_BUILD)/stub_%.cpp
	@

#-----------------------------------------------
#                 Targets
#-----------------------------------------------

stubs: $(STUB_SOURCES)

endif
