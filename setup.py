#!/usr/bin/env python

from distutils.core import setup

setup(name='xact',
      version='1.0',
      author='Christophe Pettus',
      author_email='xof@thebuild.com',
      url='https://github.com/Xof/xact',
      license='PostgreSQL',
      py_modules=['xact'],
      requires=['Django', 'psycopg2'],
      description="A recipe for handling transactions sensibly in Django applications on PostgreSQL",
      long_description=open('README.md').read()
     )
