"""
Hypothesis Testing - Educational Notebooks for Statistical Analysis

A comprehensive collection of Jupyter notebooks exploring statistical hypothesis 
testing concepts, methods, and practical applications using Python.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='hypothesis-testing',
    version='1.0.0',
    author='S Cotton',
    author_email='',
    description='Educational notebooks for statistical hypothesis testing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/scotton/hypothesis-testing',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    keywords='statistics hypothesis-testing education jupyter data-science',
    project_urls={
        'Source': 'https://github.com/scotton/hypothesis-testing',
        'Bug Reports': 'https://github.com/scotton/hypothesis-testing/issues',
    },
    include_package_data=True,
    package_data={
        'resources': ['*.csv'],
    },
)
