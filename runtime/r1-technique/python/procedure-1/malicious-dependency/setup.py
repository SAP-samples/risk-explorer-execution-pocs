# Took from https://docs.python.org/3/distutils/introduction.html#distutils-simple-example

# To create the sdist: python3.10 setup.py sdist
# Then you find the package to be distributed in the ./dist folder


from distutils.core import setup
from setuptools import setup, find_packages

setup(name='foo',
      version='1.0',
      py_modules=['foo'],
      packages = find_packages()
      )