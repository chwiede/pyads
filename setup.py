#!/usr/bin/env python
"""Pip package for chwiede.pyads
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/chwiede/pyads
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
      

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
      
from distutils.core import setup

setup(
    name='chwiede.pyads',
    version='0.1.2',
    description='python implementation of ADS protocol',
    url='http://www.github.com/chwiede/pyads',

    author='Christoph Wiedemann',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],

    keywords='beckhoff ads sps',
    packages = find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[]
)

