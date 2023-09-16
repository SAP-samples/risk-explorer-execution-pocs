"""Exploit find_packages to trigger a malicious action.

To create the sdist: python3.10 setup.py sdist
Then the package to be distributed is in ./dist folder
"""
from distutils.core import setup
from setuptools import setup, find_packages


setup(name='foo',
      version='1.0',
      py_modules=['foo'],
      packages=find_packages()
      )
