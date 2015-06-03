#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to run the tests."""

import sys
from unittest import TestLoader, TextTestRunner

# Change PYTHONPATH to include pefile.
sys.path.insert(0, u'.')

if __name__ == '__main__':
  test_suite = TestLoader().discover('./tests', pattern='*_test.py')
  test_results = TextTestRunner(verbosity=2).run(test_suite)
  if not test_results.wasSuccessful():
    sys.exit(1)
