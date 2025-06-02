from __future__ import print_function
from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop

import os
import shutil
import subprocess
import tarfile
import sys

setup(
    name='nesmdb',
    version='0.1.8',
    description='The NES Music Database (NES-MDB). Use machine learning to compose music for the Nintendo Entertainment System!',
    author='Chris Donahue',
    author_email='cdonahue@ucsd.edu',
    url='https://github.com/chrisdonahue/nesmdb',
    download_url='https://github.com/chrisdonahue/nesmdb/releases',
    license='MIT',
    packages=['nesmdb', 'nesmdb.vgm', 'nesmdb.score'],
    keywords='music nes mir midi',
    python_requires='>=2.7',
    install_requires=[
      'numpy >= 1.7.0',
      'scipy >= 1.0.0',
      'Pillow >= 5.1.0',
      'six>=1.13.0',
      'tqdm >= 4.19.9',
    ],
    test_suite='nose.collector',
    tests_require=[
      'nose >= 1.3.7',
      'pretty_midi >= 0.2.8',
      'librosa >= 0.6.1',
    ],
    entry_points = {
      'console_scripts': [
        'nesmdb_convert = nesmdb.convert:main',
      ],
    },
)
