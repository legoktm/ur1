#!/usr/bin/env python3

import sys
from setuptools import setup

py27 = sys.version[0] == '2'

setup(
    name='ur1',
    version='1.1',
    author='Kunal Mehta',
    author_email='legoktm@gmail.com',
    url='https://github.com/legoktm/ur1/',
    license='Public domain',
    description='A library to shorten urls with ur1.ca.',
    long_description=open('README.rst').read(),
    packages=['ur1'],
    test_suite='tests.ur1_test',
    install_requires=['functools32'] if py27 else [],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
)
