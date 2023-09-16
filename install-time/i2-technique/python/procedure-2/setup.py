"""
To create the sdist: python3.11 setup.py sdist
Then the package to be distributed is in ./dist folder
"""
from distutils.core import setup
from setuptools.command.install import install  # This example requires this import to be effective


class PostInstallCommand(install):
    """Malicious class triggering a post install command"""
    def run(self):
        install.run(self)
        import os; os.system("echo 'Hello World!'")  # Place any malicious code :)


setup(name='foo',
      version='1.0',
      cmdclass={
          'install': PostInstallCommand,
      },
      )
