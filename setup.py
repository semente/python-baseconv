#/usr/bin/env python

import codecs
import os
import sys

from os.path import join, dirname
from setuptools import setup


if 'publish' in sys.argv:
    os.system('python setup.py sdist upload')
    sys.exit()

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


setup(
    name='python-baseconv',
    version='1.1.2',
    description=(
        'Convert numbers from base 10 integers to base X strings '
        'and back again.'
    ),
    long_description=read(join(dirname(__file__), 'README.rst')),
    keywords='converter numbers math',
    author='Drew Perttula, Guilherme Gondim, Simon Willison',
    author_email='semente+baseconv@taurinus.org',
    maintainer='Guilherme Gondim',
    maintainer_email='semente+baseconv@taurinus.org',
    license='Python Software Foundation License',
    url='https://bitbucket.org/semente/baseconv/',
    download_url='https://bitbucket.org/semente/baseconv/downloads/',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['baseconv'],
)
