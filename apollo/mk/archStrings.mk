# This lookup table specifies the asinine "architecture string" (in 2 versions, v1 and v2) that is part of each dep's name.
# "architecture string"s are arbitrary and often not correct, this table lets apollo map each dep to its own style
#   Note 1: that an artifact is expected for both architectures, so in the case of the airmailDaemon or SR-Util where only
#           one architecture exists, just specify that architecture for both
#   Note 2: make these names consistent with ALL_DEPS list so they can be referenced from foreach

# Map each repository to the architecture string it uses
airBoot_x86DArch            = cygGcc
airBoot_armArch             = armUios
airFrame_x86DArch           = winMsvcD
airFrame_x86Arch            = winMsvc
airFrame_armArch            = armUios
airFrame_x86LinuxArch       = linuxGcc
CppUTest_x86DArch           = winMsvcD
CppUTest_armArch            = armUios
gnc_x86DArch                = winMsvcD
gnc_x86Arch                 = winMsvc
gnc_armArch                 = armUios
hades_x86DArch              = cygGcc
hades_armArch               = armUios
libTomCrypt_x86DArch        = winMsvcD
libTomCrypt_armArch         = armUios
libTomCrypt_x86LinuxArch    = linuxGcc
lwip_x86DArch               = cygGcc
lwip_armArch                = armUcos
mfgMessages_x86DArch        = cygGcc
mfgMessages_armArch         = armUios
micrium_x86DArch            = cygGcc
micrium_armArch             = armUios
nanopb_x86DArch             = winMsvcD
nanopb_x86Arch              = winMsvc
nanopb_armArch              = armUios
nanopb_x86LinuxArch         = linuxGcc
stlib_x86DArch              = cygGcc
stlib_armArch               = armUios
systemMessages_x86DArch     = winMsvcD
systemMessages_x86Arch      = winMsvc
systemMessages_armArch      = armUios
systemMessages_x86LinuxArch = linuxGcc
uios_x86DArch               = winMsvcD
uios_x86Arch                = winMsvc
uios_armArch                = armUcos
uios_x86LinuxArch           = linuxGcc

# These components are only available for a single architecture but the scripts expect an arm and x86 version
# work around this by specifying the same architecture for each (results in dep being downloaded twice)
airmailDaemon_x86DArch  = winMsvcD
airmailDaemon_armArch   = winMsvcD
jsbsim_x86DArch         = winMsvcD
jsbsim_x86Arch          = winMsvc
jsbsim_armArch          = winMsvcD
SRUtil_x86DArch         = none
SRUtil_armArch          = none
SRUtil_x86LinuxArch     = none

cygGcc_v1   = x86_64-cygwin-gcc
cygGcc_v2   = x8664cygwingcc
linuxGcc_v1 = x86_64-linux-gcc
linuxGcc_v2 = x8664linuxgcc
winMsvc_v1  = x86_64-win-msvc-release
winMsvc_v2  = x8664winmsvc
winMsvcD_v1 = x86_64-win-msvc
winMsvcD_v2 = x8664winmsvc
armUios_v1  = arm-uios-keil-m4
armUios_v2  = armuioskeilm4
armUcos_v1  = arm-ucos2-keil-m4
armUcos_v2  = armucos2keilm4
none_v1     = none
none_v2     = none
