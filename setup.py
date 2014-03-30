#!/usr/bin/env python

""" Setup file for django-beautifulsoup-test. """

from pip.req import parse_requirements
from distutils.core import setup
import os

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs if ir.req]

setup(name='django-beautifulsoup-test',
      version='1.0',
      description='TestCase class for using BeautifulSoup with Django tests',
      author='Jonathan Scott',
      author_email='jonathan@jscott.me',
      url='https://github.com/jscott1989/django-beautifulsoup-test',
      packages=[x[0] for x in os.walk('django_bs_test')],
      install_requires=reqs,
      )
