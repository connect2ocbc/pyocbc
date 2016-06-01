#!/usr/bin/env python
"""The setup and build script for the pyocbc library."""

import codecs
import ocbc
from setuptools import setup, find_packages


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

with codecs.open('README.rst', 'r', 'utf-8') as fd:
    setup(name='pyocbc',
          version=ocbc.__version__,
          author='Naveen Hegde',
          author_email='naveen.sanmane@gmail.com',
          license='LGPLv3',
          url='https://github.com/connect2ocbc/pyocbc',
          keywords='ocbc api wrapper',
          description='A new way of banking',
          long_description=fd.read(),
          packages=find_packages(exclude=['tests*']),
          install_requires=requirements(),
          include_package_data=True,
          classifiers=[
              'Development Status :: 5 - Production/Stable',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
              'Operating System :: OS Independent',
              'Topic :: Software Development :: Libraries :: Python Modules',
              'Topic :: Communications :: Api',
              'Topic :: Internet',
              'Programming Language :: Python :: 2.7',
          ],)
