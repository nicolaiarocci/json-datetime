#!/usr/bin/env python

from setuptools import setup, find_packages

from jsondatetime import __version__
DESCRIPTION = ("Allows for proper decoding of datetime values contained in "
               "JSON streams")
LONG_DESCRIPTION = open('README.md').read()

setup(name='jsondatetime',
      version=__version__,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='Nicola Iarocci',
      author_email='nicola@nicolaiarocci.com',
      url='http://github.com/nicolaiarocci/json-datetime',
      license="MIT License",
      platforms=["any"],
      packages=find_packages(),
      test_suite="jsondatetime.tests",
     )
