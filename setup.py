#!/usr/bin/python

import ast
import os
import re
import sys
from unittest import TestLoader, TextTestRunner

from setuptools import Command, setup


os.environ["COPY_EXTENDED_ATTRIBUTES_DISABLE"] = "true"
os.environ["COPYFILE_DISABLE"] = "true"


def _read_doc():
    """
    Parse docstring from file 'pefile.py' and avoid importing
    this module directly.
    """
    with open("pefile.py", "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    return ast.get_docstring(tree)


def _read_attr(attr_name):
    """
    Parse attribute from file 'pefile.py' and avoid importing
    this module directly.

    __version__, __author__, __contact__,
    """
    regex = attr_name + r"\s+=\s+['\"](.+)['\"]"
    with open("pefile.py", "r", encoding="utf-8") as f:
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

    def run(self):
        test_suite = TestLoader().discover("./tests", pattern="*_test.py")
        test_results = TextTestRunner(verbosity=2).run(test_suite)


setup(
    name="pefile",
    version=_read_attr("__version__"),
    description="Python PE parsing module",
    author=_read_attr("__author__"),
    author_email=_read_attr("__contact__"),
    url="https://github.com/erocarrera/pefile",
    download_url="https://github.com/erocarrera/pefile/releases/download/v2024.8.26/pefile-2024.8.26.tar.gz",
    keywords=["pe", "exe", "dll", "pefile", "pecoff"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description="\n".join(_read_doc().split("\n")),
    cmdclass={"test": TestCommand},
    py_modules=["pefile", "peutils"],
    python_requires=">=3.6.0",
    packages=["ordlookup"],
    install_requires=[],
    license="MIT",
)
