#!/usr/bin/env python

import os.path
import sys
from glob import glob


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readme():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
            return f.read()
    except (IOError, OSError):
        return ''


setup(
    name='mlab',
    version='1.1.1',
    description='Mlab is a high-level python to Matlab® bridge that lets Matlab look like a normal python library',
    long_description=readme(),
    author='Yauhen Yakimovich',
    author_email='eugeny.yakimovitch@gmail.com',
    url='https://github.com/ewiger/mlab',
    license='MIT',
    packages=['mlab'],
    package_dir={
        'mlab': 'src/mlab',
    },
    download_url='https://github.com/ewiger/mlab/tarball/master',
)

