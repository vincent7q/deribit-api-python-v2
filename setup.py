"""DERIBIT API Module.
See:
https://docs.deribit.com/v2/
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='deribit_api_v2',

    version='1.2',

    description='API Client for Deribit API verions 2',
    long_description=long_description,

    url='https://github.com/deribit/deribit-api-v2-python',

    license='MIT',

    author="Vincent Choy",
    author_email="vincent7q@gmail.com",


    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    keywords='deribit api',

    py_modules=["deribit_api"],

    install_requires=['requests'],

)
