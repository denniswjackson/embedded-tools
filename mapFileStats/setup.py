#!/usr/bin/env python

from distutils.core import setup
from mapFileStats import __version__

setup(name='mapFileStats',
      version=__version__,
      description='Parses Keil map files and outputs stats for RAM and ROM usage, tailored for TeamCity tracking',
      author='Dennis W. Jackson',
      author_email='djackson@airware.com',
      scripts=['mapFileStats.py'],
     )
