#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import sys


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.match("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('django_rest_model_hyperlink_serializers/hyperlinked_relational_serializer')


setup(
    name='djangorestrelationalhyperlink',
    version=version,
    url='http://django-rest-framework.org',
    license='BSD',
    description='A hyperlinked serialiser that can can be used to alter relationships via hyperlinks, but otherwise like a hyperlink model serializer',
    author='Fred Kingham',
    author_email='fredkingham@gmail.com',  # SEE NOTE BELOW (*)
    packages=['django_rest_model_hyperlink_serializers.hyperlinked_relational_serializer'],
    test_suite='django_rest_model_hyperlink_serializers.hyperlinked_relational_serializer.hl_relational_serializer_tests.runtests',
    install_requires=['djangorestframework(>=2.3.6)'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

