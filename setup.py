#!/usr/bin/env python

from setuptools import setup, find_packages


with open('README.rst') as file:
    readme = file.read()


setup(
    name='Flask-DB2',
    version='0.0.10',
    url='http://github.com/juztin/flask-db2',
    license='BSD',
    author='Justin Wilson',
    author_email='justin@minty.io',
    description='Creates connections for use with DB2',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.9'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3 :: Only",
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
