#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, Command
except ImportError, excp:
    from distutils.core import setup, Command

from unittest import TestLoader, TextTestRunner

import pefile
import os

# os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
# os.environ['COPYFILE_DISABLE'] = 'true'

class TestCommand(Command):
  """Run tests."""
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    test_suite = TestLoader().discover('./tests', pattern='*_test.py')
    test_results = TextTestRunner(verbosity=2).run(test_suite)

setup(name = 'pefile',
    version = pefile.__version__,
    description = 'Python PE parsing module',
    author = pefile.__author__,
    author_email = pefile.__contact__,
    url = 'https://github.com/erocarrera/pefile',
    download_url='https://github.com/erocarrera/pefile/tarball/master',
    keywords = ['pe', 'exe', 'dll', 'pefile', 'pecoff'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
    	'Intended Audience :: Developers',
    	'Intended Audience :: Science/Research',
    	'Natural Language :: English',
    	'Operating System :: OS Independent',
    	'Programming Language :: Python',
    	'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description = "\n".join(pefile.__doc__.split('\n')),
    cmdclass={"test": TestCommand},
    py_modules = ['pefile', 'peutils'],
    packages = ['ordlookup'] )

