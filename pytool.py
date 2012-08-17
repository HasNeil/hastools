#!/usr/bin/python

import sys
import sysconfig
import os

print "Platform:\t\t%s" % (sys.platform)
print "Version:\t\t%s" % (sys.version)
print "Subversion:\t\t", sys.subversion
print "Version Info:\t\t%s" % (sys.version_info)
print "API Version:\t\t%s" % (sys.api_version)
print "Modules:\t\t%s" % (sys.modules)
print "Path:\t\t%s" % (sys.path)
print "Max. Int:\t\t%s" % (sys.maxint)
print "Max Size:\t\t%s" % (sys.maxsize)
print "Max. Unicode:\t\t%s" % (sys.maxunicode)
print "Filesystem Encoding:\t\t", sys.getfilesystemencoding()
print "Default Encoding:\t\t", sys.getdefaultencoding()
print "Executable:\t\t%s" % (sys.executable)
print "Flags:\t\t%s" % (sys.flags)
print "Built In Module Names:\t\t", sys.builtin_module_names
print "ByteOrder:\t\t%s" % (sys.byteorder)
print sysconfig.get_platform()
print sysconfig.is_python_build()
print sysconfig.get_path_names()
print sysconfig.get_scheme_names()
##print sysconfig.get_config_vars()
for var in sysconfig.get_config_vars().keys():
  print var.lower(), ":", sysconfig.get_config_vars(var)
print os.name

import fileinput
for line in fileinput.input('/etc/mtab'):
    print line,
