#!/usr/bin/env python

from setuptools import find_packages, setup

DESCRIPTION = (
    "Allows for encoding and decoding of datetime values contained in JSON streams"
)
LONG_DESCRIPTION = open("README.rst").read()

setup(
    name="jsondatetime",
    version="0.1.0",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    # Forked.
    #  Original author='Nicola Iarocci',
    #  Original author_email='nicola@nicolaiarocci.com',
    #  Original url='http://github.com/nicolaiarocci/json-datetime',
    author="Andrew Stribblehill",
    author_email="andrew.stribblehill@schibsted.com",
    url="https://github.com/schibsted/json-datetime",
    license=open("LICENSE").read(),
    platforms=["any"],
    packages=find_packages(),
    test_suite="jsondatetime.tests",
    install_requires=["simplejson;python_version<'2.7'", "python-dateutil"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
