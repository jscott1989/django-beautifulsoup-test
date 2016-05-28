#!/usr/bin/env python

""" Setup file for django-beautifulsoup-test. """

from setuptools import setup
import os

setup(name='django-beautifulsoup-test',
      version='1.1.0',
      description='TestCase class for using BeautifulSoup with Django tests',
      author='Jonathan Scott',
      author_email='jonathan@jscott.me',
      url='https://github.com/jscott1989/django-beautifulsoup-test',
      packages=[x[0] for x in os.walk('django_bs_test')],
      install_requires=["beautifulsoup4", "django"]
      )
