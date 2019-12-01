"""
Install dataset downloader.
"""
from setuptools import setup, find_packages
from distutils.core import setup
from distutils.extension import Extension

# Define the minimal classes needed to install and run utilkg
INSTALL_REQUIRES = []

# Define the package data we need
PACKAGE_DATA = {}

cmdclass = {}
ext_modules = []

# Run the setup
setup(name='datasets',
      version='1.0.0',
      packages=find_packages('.'),
      package_data=PACKAGE_DATA,
      description='Dataset downloader for onsite',
      author='jose',
      author_email='jose@util.co',
      install_requires=INSTALL_REQUIRES,
      test_suite='tests',
      cmdclass=cmdclass,
      ext_modules=ext_modules)
