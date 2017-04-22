#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import soccer

from setuptools import setup, find_packages

with open('README.rst', 'rb') as f_readme:
    readme = f_readme.read().decode('utf-8')

packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

setup(
    name='pysoccer',
    version=soccer.__version__,
    keywords=['soccer', 'football', 'football-data'],
    description='Soccer data for programmers.',
    long_description=readme,
    author='RayYu03',
    author_email='shiliuhuasheng@gmail.com',
    license='MIT',
    url='https://github.com/RayYu03/pysoccer',
    install_requires=['requests','click'],
    packages=packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Information Technology',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points={
        'console_scripts': [
            'soccer = soccer.main:main'
        ]
    }
)
