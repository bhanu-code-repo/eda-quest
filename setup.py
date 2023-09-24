# -*- coding: utf-8 -*-

# Import setuptools
from setuptools import setup, find_packages

# Setup the package
setup(
    name='eda-quest',
    version='0.0.1',
    description='Exploratory Data Analysis Package - Swiss Knife for Data Science',
    author='Bhanu Thakur',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn'
    ],
)