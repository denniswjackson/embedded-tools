# If this module has not been included from another, import Apollo Makefile
ifndef BASE
    include ../Makefile
else
    include $(MK_DIR)/archStrings.mk


#---------------------------------------------
#       Set up external dependencies
#---------------------------------------------

# The list of dependencies. These names must correspond to the package names in team city
#    As long as the GNC repo distributes multiple packages, it must be handled differently. Once it is standardized, these lists can be merged into ALL_DEPS
STD_DEPS = airFrame hades lwip micrium nanopb jsbsim SRUtil stlib systemMessages uios mfgMessages airmailDaemon CppUTest libTomCrypt
GNC_DEPS = control navigation
LINUX_DEPS = airFrame libTomCrypt nanopb SRUtil systemMessages uios
ALL_DEPS = $(STD_DEPS) $(GNC_DEPS)

# The list of dependencies which produce a release version library which the sim must link against
STD_RELEASE_DEPS = airFrame nanopb jsbsim systemMessages uios
GNC_RELEASE_DEPS = control navigation
RELEASE_DEPS = $(STD_RELEASE_DEPS) $(GNC_RELEASE_DEPS)

# Versions of external dependencies (make these names consistent with ALL_DEPS list so they can be referenced from foreach)

airFrame_VERSION       = 1.64.0
airmailDaemon_VERSION  = 2.27.0
CppUTest_VERSION       = 3.4.112
gnc_VERSION            = 3.0.0
hades_VERSION          = 1.28.0
jsbsim_VERSION         = 1.6.0
libTomCrypt_VERSION    = 1.17.103
lwip_VERSION           = 1.4.209
mfgMessages_VERSION    = 1.2.0
micrium_VERSION        = 1.9.0
nanopb_VERSION         = 1.1.3
SRUtil_VERSION         = 1.0.0
stlib_VERSION          = 1.3.106
systemMessages_VERSION = 3.2.0
uios_VERSION           = 1.68.0

airFrame_BRANCH        =
airmailDaemon_BRANCH   =
CppUTest_BRANCH        =
gnc_BRANCH             = develop
hades_BRANCH           =
jsbsim_BRANCH          =
libTomCrypt_BRANCH     =
lwip_BRANCH            =
mfgMessages_BRANCH     =
micrium_BRANCH         =
nanopb_BRANCH          =
stlib_BRANCH           =
systemMessages_BRANCH  = develop
uios_BRANCH            =

# Deps get loaded here
DEPS = $(BASE)/deps

# The depsPresent files are just a marker of when deps were last fetched. It must be present for compilation steps to run
# They depends on the readme.md files of each dependency, since these contain the version (so that a version increase triggers a rebuild)
$(DEPS)/x86DDepsPresent: $(foreach dep, $(ALL_DEPS), $(DEPS)/$(dep)-x86D/readme_$($(dep)_VERSION).md )
	touch $@
$(DEPS)/armDepsPresent: $(foreach dep, $(ALL_DEPS), $(DEPS)/$(dep)-arm/readme_$($(dep)_VERSION).md )
	touch $@
$(DEPS)/x86DepsPresent: $(foreach dep, $(RELEASE_DEPS), $(DEPS)/$(dep)-x86/readme_$($(dep)_VERSION).md )
	touch $@
$(DEPS)/x86LinuxDepsPresent: $(foreach dep, $(LINUX_DEPS), $(DEPS)/$(dep)-x86Linux/readme_$($(dep)_VERSION).md )
	touch $@

deps: $(DEPS)/armDepsPresent $(DEPS)/x86DDepsPresent $(DEPS)/x86DepsPresent $(DEPS)/x86LinuxDepsPresent

# Remove all folders and present indicators
clean_deps:
	rm -rf $(BASE)/deps

# Create include paths for bringing in external includes (note that release and debug include paths are identical)
EXT_X86_INCLUDE_PATH =   $(foreach dep,$(ALL_DEPS), $(DEPS)/$(dep)-x86D/include) $(DEPS)/lwip-x86D/include/ipv4 $(DEPS)/lwip-x86D/include/posix $(DEPS)/hades-x86D/src/tcpip/lwip
EXT_ARM_INCLUDE_PATH  = $(foreach dep,$(ALL_DEPS), $(DEPS)/$(dep)-arm/include) $(DEPS)/lwip-arm/include/ipv4 $(DEPS)/lwip-arm/include/posix $(DEPS)/hades-arm/src/tcpip/lwip

#-----------------------------------------------------------------------------------------------------------------------------------------
# Commands to import external dependencies
#  $(1) = repository name
#  $(2) = architecture name
#  $(3) = dependency name
#  *Start by wiping old version
#  *Make a new folder, if these first two steps are omitted the operation will occasionally fail on windows due to "insufficient permissions"
#  *Download new version to folder
#  *touch it so that make sees it is up to date next time
#-----------------------------------------------------------------------------------------------------------------------------------------
GET_DEP_CMD = curl -u guest: --fail
define GET_DEP
$$(DEPS)/$(3)-$(2)/readme_$$($(3)_VERSION).md:
	mkdir -p $(DEPS)
	rm -rf $$(DEPS)/$(3)-$(2)
	mkdir -p $$(DEPS)/$(3)-$(2)
ifdef $(1)_BRANCH
	if ! $(GET_DEP_CMD) $$($(1)_$(2)_$(3)_branchURL) | tar zx -C $$(DEPS)/$(3)-$(2) --strip-components=1; \
	then \
		$(GET_DEP_CMD) $($(1)_$(2)_$(3)_supportURL) | tar zx -C $$(DEPS)/$(3)-$(2) --strip-components=1; \
	fi
else
	$(GET_DEP_CMD) $($(1)_$(2)_$(3)_masterURL) | tar zx -C $$(DEPS)/$(3)-$(2) --strip-components=1
endif
	touch $$@
endef

# And a command for constructing the standard-form URLS, which will be stored in $(1)_$(2)_$(3)_URL. They are stored separately since some need to be overridden
# If repo_BRANCH is defined, then two add additional pieces are added to URL
# Note that arguments $(1) and $(3) will be the same in all cases except for control and navigation which are both distrubted from the GNC project
define MAKE_DEP_URL
 $(1)_$(2)_$(3)_branchURL = http://teamcity/repository/download/$(1)_package_$$($$($(1)_$(2)Arch)_v2)/.lastSuccessful/$(3)-$$($(1)_VERSION)-$$($$($(1)_$(2)Arch)_v1).tar.gz?branch=$$($(1)_BRANCH)
 $(1)_$(2)_$(3)_supportURL = http://teamcity/repository/download/$(1)_package_$$($$($(1)_$(2)Arch)_v2)/$$($(1)_VERSION).tcbuildtag/$(3)-$$($(1)_VERSION)-$$($$($(1)_$(2)Arch)_v1).tar.gz?branch=$$($(1)_BRANCH)
 $(1)_$(2)_$(3)_masterURL = http://teamcity/repository/download/$(1)_package_$$($$($(1)_$(2)Arch)_v2)/$$($(1)_VERSION).tcbuildtag/$(3)-$$($(1)_VERSION)-$$($$($(1)_$(2)Arch)_v1).tar.gz
endef

# Loop through all standard dependencies, building the url, and the rule for retrieving the url
$(foreach dep,$(STD_DEPS),$(eval $(call MAKE_DEP_URL,$(dep),x86D,$(dep))))
$(foreach dep,$(STD_DEPS),$(eval $(call MAKE_DEP_URL,$(dep),arm,$(dep))))
$(foreach dep,$(STD_RELEASE_DEPS),$(eval $(call MAKE_DEP_URL,$(dep),x86,$(dep))))
$(foreach dep,$(STD_DEPS),$(eval $(call GET_DEP,$(dep),x86D,$(dep))))
$(foreach dep,$(STD_DEPS),$(eval $(call GET_DEP,$(dep),arm,$(dep))))
$(foreach dep,$(STD_RELEASE_DEPS),$(eval $(call GET_DEP,$(dep),x86,$(dep))))

# Loop through all GNC dependencies, building the url, and the rule for retrieving the url
$(foreach dep,$(GNC_DEPS),$(eval $(call MAKE_DEP_URL,gnc,x86D,$(dep))))
$(foreach dep,$(GNC_DEPS),$(eval $(call MAKE_DEP_URL,gnc,arm,$(dep))))
$(foreach dep,$(GNC_RELEASE_DEPS),$(eval $(call MAKE_DEP_URL,gnc,x86,$(dep))))
$(foreach dep,$(GNC_DEPS),$(eval $(call GET_DEP,gnc,x86D,$(dep))))
$(foreach dep,$(GNC_DEPS),$(eval $(call GET_DEP,gnc,arm,$(dep))))
$(foreach dep,$(GNC_RELEASE_DEPS),$(eval $(call GET_DEP,gnc,x86,$(dep))))

# Loop through all Linux dependencies, building the url, and the rule for retrieving the url
$(foreach dep,$(LINUX_DEPS),$(eval $(call MAKE_DEP_URL,$(dep),x86Linux,$(dep))))
$(foreach dep,$(LINUX_DEPS),$(eval $(call GET_DEP,$(dep),x86Linux,$(dep))))

endif
