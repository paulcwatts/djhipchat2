#!/usr/bin/env python
import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djhipchat2',
    version='0.5',
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
    ]
)
