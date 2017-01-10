# this file is never called alone and is always included from the top-level Makefile
include $(MK_DIR)/version.mk

RUNAWXTOOL = $(PYTHON_TOOLS_DIR)/runAwxTool.py

# location of local signing and encryption keys
AWX_KEYDIR = $(BASE)/keys

#-----------------------------------------------
#           VID / PID Definitions
# Ref http://confluence/display/AIR/Production+Parameters+and+Test+Lifecycle+Data+Board+ICD
#-----------------------------------------------
AIRWARE_VID             = 0x0001
FC_PID                  = 0x0001
AC_PID                  = 0x0002
GDM_IPNDDL2450_EXP_PID  = 0x0003
ASM_PID                 = 0x0005
GPS_PID                 = 0x0006
ACT04P_PID              = 0x0007
ADM_IPNDDL2450_EXP_PID  = 0x0008
AGL_PID                 = 0x0009
GDM_IPNDDL2450_PID      = 0x000C
GDM_N2420BF_PID         = 0x000D
GDM_N920F_PID           = 0x000E
GDM_N920F_AUS_PID       = 0x000F
ADM_N2420BF_PID         = 0x0020
ADM_N920F_PID           = 0x0021
ADM_IPNDDL2450_PID      = 0x0022
ADM_N920F_AUS_PID       = 0x0023
ACT12P_PID              = 0x0024
AGL_LEDDAR_PID          = 0x0026
PKID_PID                = 0xFFF0

#---------------------------------------------------------------
#    awx generation (signing / encryption)
#
# AWX_SIGNING_KEYNAME    - keyname to use for signing; the board
#                          bootloaders require that all awx images
#                          be signed
# AWX_ENCRYPTION_KEYNAME - keyname to use for encryption; the board
#                          bootloaders will accept an awx image that
#                          is not encrypted
# AWXTOOL_KEYARGS        - all key-related CLI parameters
#                          that are passed to awxTool
# AWXTOOL_NONKEYARGS     - non-key-related CLI parameters
#                          that are passed to awxTool
# AXWTOOL_BINVERSION     - version info written to awx header
# AWXTOOL_IMAGETYPE      - specifies the image type to
#                          generate in the awx file
# AWX_OUTPUT_DIR         - output directory for awx files
#                          (relative to $(OUTPUT))
# AWXTOOL_USER_ARGS      - CLI arguments that the build
#                          tooling is expected to set to
#                          generate a specific configuration
# For example (all on one line):
#  $ make hexes AWXTOOL_USER_ARGS='--signingKeyName s01FwDv
#                                  --encryptionKeyName e01FwDv
#                                  --keyDir key
#                                  --useHsm 1'
#---------------------------------------------------------------

# define the keynames used for signing and encryption
AWX_SIGNING_KEYNAME    =  s01FwDv
AWX_ENCRYPTION_KEYNAME =  e01FwDv

# the following arguments should not have to be modified
# Note: Ref INFR-383 a bug in awxtool chokes if you specify "--useHsm 0", however it does default safely to 0 if omitted
AWXTOOL_KEYARGS    =  --keyDir $(AWX_KEYDIR)
AWXTOOL_KEYARGS    += --signingKeyName $(AWX_SIGNING_KEYNAME)
# comment out the following line if you don't want to encrypt the image
AWXTOOL_KEYARGS    += --encryptionKeyName $(AWX_ENCRYPTION_KEYNAME)
AWXTOOL_NONKEYARGS =  --targetVendorId $(AIRWARE_VID)
AXWTOOL_BINVERSION =  $(VERSION_MAJOR).$(VERSION_MINOR).$(VERSION_PATCH).$(BUILD_NUMBER)
AWXTOOL_BINVERARGS =  --binVersion $(AXWTOOL_BINVERSION)
AWXTOOL_IMAGETYPE  =  app
AWXTOOL_IMAGEARGS  =  --imageType $(AWXTOOL_IMAGETYPE)
AWXTOOL_USER_ARGS  =  $(AWXTOOL_KEYARGS)
AWXTOOL_ARGS       =  $(AWXTOOL_NONKEYARGS) $(AWXTOOL_IMAGEARGS) $(AWXTOOL_USER_ARGS) $(AWXTOOL_BINVERARGS)
AWX_OUTPUT_DIR     =  .
