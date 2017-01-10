#-----------------------------------------------
#                 Debugging
#-----------------------------------------------
# Source: http://blog.jgc.org/2015/04/the-one-line-you-should-add-to-every.html
print-%: ; @echo $*=$($*)

# List all targets.  Source: http://stackoverflow.com/a/15058900/346
# Note: there are some targets that are listed that are not valid. It's not perfect.
# It's also just for debugging and remembering the lower level targets.
.PHONY: no_targets__ list
no_targets__:
list:
	sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | sort"


# See all Makefile variables
# This breaks in a Windows command prompt in Apollo calling cygwin utils but worked from a mingw64 prompt.
# Source: http://stackoverflow.com/a/7144684/346
# Call out sort path to avoid collision with the Windows version
debug_printAllVars:
	$(MAKE) -pn | grep -A1 "^# makefile"| grep -v "^#\|^--" | /usr/bin/sort | uniq > vars.txt
