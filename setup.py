#!/usr/bin/python

import ast
import os
import re
import sys

if sys.version_info.major == 3:
    from io import open

try:
    from setuptools import setup, Command
except ImportError as excp:
    from distutils.core import setup, Command

from unittest import TestLoader, TextTestRunner


os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'


def _read_doc():
    """
    Parse docstring from file 'pefile.py' and avoid importing
    this module directly.
    """
    if sys.version_info.major == 2:
        with open('pefile.py', 'r') as f:
            tree = ast.parse(f.read())
    else:
        with open('pefile.py', 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
    return ast.get_docstring(tree)


def _read_attr(attr_name):
    """
    Parse attribute from file 'pefile.py' and avoid importing
    this module directly.

    __version__, __author__, __contact__,
    """
    regex = attr_name + r"\s+=\s+'(.+)'"
    if sys.version_info.major == 2:
        with open('pefile.py', 'r') as f:
            match = re.search(regex, f.read())
    else:
        with open('pefile.py', 'r', encoding='utf-8') as f:
            match = re.search(regex, f.read())
    # Second item in the group is the value of attribute.
    return match.group(1)


class TestCommand(Command):
  """Run tests."""
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

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
    version = _read_attr('__version__'),
    description = 'Python PE parsing module',
    author = _read_attr('__author__'),
    author_email = _read_attr('__contact__'),
    url = 'https://github.com/erocarrera/pefile',
    download_url='https://github.com/erocarrera/pefile/releases/download/v2017.11.5/pefile-2017.11.5.tar.gz',
    keywords = ['pe', 'exe', 'dll', 'pefile', 'pecoff'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description = "\n".join(_read_doc().split('\n')),
    cmdclass={"test": TestCommand},
    py_modules = ['pefile', 'peutils'],
    packages = ['ordlookup'],
    install_requires=[
          'future',
    ],
)
