#!/usr/bin/env python
from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

version='0.1'

setup(
    name='django-admin-decorators',
    version=version,
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['admin_decorators'],
    url='https://bitbucket.com/kmike/django-admin-decorators/',
    license = 'MIT license',
    description = """ Extra decorators for django admin """,

    long_description = open('README.rst').read(),
    requires = ['django'],

    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
