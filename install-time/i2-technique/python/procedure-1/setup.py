# Took from https://docs.python.org/3/distutils/introduction.html#distutils-simple-example

# To create the sdist: python3.11 setup.py sdist
# Then you find the package to be distributed in the ./dist folder


from setuptools import setup

import os; os.system("echo 'Hello World!'")      # Place any malicious code :)


setup(name='foo',
      version='1.0',
      py_modules=['foo'],
      )
