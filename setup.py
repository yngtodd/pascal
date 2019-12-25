#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Todd Young",
    author_email='young.todd.mk@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="A Pascal interpreter written in Python",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pascal',
    name='pascal',
    packages=find_packages(),
    setup_requires=setup_requirements,
    entry_points={
        'console_scripts': [
            'pascal = pascal.pascal:main',
        ],
    },
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yngtodd/pascal',
    version='0.1.0',
    zip_safe=False,
)
