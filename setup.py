#!/usr/bin/env python

import os
import sys
import subprocess
import string

from distutils.core import setup, Extension

if os.name == "posix":
  from mariadb_posix import get_config

cfg= get_config()

setup(name='mariadb',
     version='0.9.1',
     description='Python MariaDB extension',
     author='Georg Richter',
     license='LGPL 2.1',
     url='http://www.mariadb.com',
     ext_modules=[Extension('mariadb', ['src/mariadb.c', 'src/mariadb_connection.c', 'src/mariadb_exception.c', 'src/mariadb_cursor.c', 'src/mariadb_codecs.c', 'src/mariadb_field.c', 'src/mariadb_dbapitype.c', 'src/mariadb_indicator.c'],
     include_dirs=cfg.includes,
     library_dirs= cfg.lib_dirs,
     libraries= cfg.libs
     )],
     )
