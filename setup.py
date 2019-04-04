#/usr/bin/env python

import codecs
import os
import sys

from os.path import join, dirname
from setuptools import setup


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()
version = __import__('baseconv').__version__

if 'publish' in sys.argv:
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='python-baseconv',
    version=version,
    description=(
        'Convert numbers from base 10 integers to base X strings '
        'and back again.'
    ),
    long_description=read(join(dirname(__file__), 'README.rst')),
    keywords='converter numbers math',
    author='Drew Perttula, Guilherme Gondim, Simon Willison',
    maintainer='Guilherme Gondim',
    license='Python Software Foundation License',
    url='https://github.com/semente/python-baseconv',
    download_url='https://github.com/semente/python-baseconv/releases',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['baseconv'],
)
