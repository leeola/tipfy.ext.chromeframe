# -*- coding: utf-8 -*-
"""
    tipfy.ext.chromeframe
    ~~~~~~~~~~~~~~~~~~~~~

    Implements the server side requirements for Chrome Frame usage in clients.

    :copyright: 2010 Lee Olayvar.
    :license: MIT, see LICENSE.txt for more details.
"""
from setuptools import setup

setup(
    name = 'tipfy.ext.chromeframe',
    version = '0.0.1',
    license = 'MIT',
    url = 'http://github.com/leeolayvar/tipfy.ext.chromeframe',
    description = 'Implements the server side requirements for Chrome Frame usage in clients.',
    long_description = __doc__,
    author = 'Lee Olayvar',
    author_email = 'leeolayvar@gmail.com',
    zip_safe = False,
    platforms = 'any',
    packages = [
        'tipfy',
        'tipfy.ext',
    ],
    namespace_packages = [
        'tipfy',
        'tipfy.ext',
    ],
    include_package_data = True,
    install_requires = [
        'tipfy',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)