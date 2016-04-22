from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='countries_from_coordinates',
    version='0.0.1',
    description='A simple package to read coordinates files and transform them to countries',
    long_description=long_description,
    url='https://github.com/che0/countries',
    author='che0',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
