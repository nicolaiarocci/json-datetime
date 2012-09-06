#!/usr/bin/env python

from setuptools import setup, find_packages
#from jsondatetime import __version__

DESCRIPTION = ("Allows for proper decoding of datetime values contained in "
               "JSON streams")
LONG_DESCRIPTION = open('README.md').read()

setup(
      name='JSON-Datetime',
      version='0.0.1',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='Nicola Iarocci',
      author_email='nicola@nicolaiarocci.com',
      url='http://github.com/nicolaiarocci/json-datetime',
      license=open('LICENSE').read(),
      platforms=["any"],
      packages=find_packages(),
      test_suite="jsondatetime.tests",
      requires=['simplejson'],
      install_requires=['simplejson'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: ISC License (ISCL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
     )
