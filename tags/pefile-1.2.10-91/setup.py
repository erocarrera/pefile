#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError, excp:
    from distutils.core import setup
    
import pefile
import os

os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'


setup(name = 'pefile',
    version = pefile.__version__,
    description = 'Python PE parsing module',
    author = pefile.__author__,
    author_email = pefile.__contact__,
    url = 'http://code.google.com/p/pefile/',
    download_url = 'http://pefile.googlecode.com/files/pefile-%s.tar.gz' % pefile.__version__,
    platforms = ['any'],
    classifiers = ['Development Status :: 5 - Production/Stable',
    	'Intended Audience :: Developers',
    	'Intended Audience :: Science/Research',
    	'Natural Language :: English',
    	'Operating System :: OS Independent',
    	'Programming Language :: Python',
    	'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description = "\n".join(pefile.__doc__.split('\n')),
    py_modules = ['pefile', 'peutils'] )

