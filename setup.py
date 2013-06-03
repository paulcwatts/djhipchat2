#!/usr/bin/env python
import os
import codecs
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if os.path.exists('README.rst'):
    long_description = codecs.open('README.rst', 'r', 'utf-8').read()
else:
    long_description = 'See https://github.com/paulcwatts/djhipchat2'

setup(
    name='djhipchat2',
    version='0.5.1',
    packages=[
        'djhipchat',
        'djhipchat.backends',
        'djhipchat.management',
        'djhipchat.management.commands'
    ],
    url='https://github.com/paulcwatts/djhipchat2',
    license='BSD',
    author='Paul Watts',
    author_email='paulcwatts@gmail.com',
    description='The most complete and configurable HipChat library for Django.',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'
    ],
    long_description=long_description
)
