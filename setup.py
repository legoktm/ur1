#!/usr/bin/env python3
from setuptools import setup

setup(
    name='ur1',
    version='0.1',
    author='Kunal Mehta',
    author_email='legoktm@gmail.com',
    url='https://github.com/legoktm/ur1/',
    license='Public domain',
    description='A library to shorten urls with ur1.ca.',
    long_description=open('README.rst').read(),
    packages=['ur1'],
    test_suite='tests.ur1_test',
)
