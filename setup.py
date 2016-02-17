import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DESCRIPTION = "Galaxy Cluster and Weak Lensing Tools"
LONG_DESCRIPTION = """
clusterlensing: galaxy cluster halo calculations
======================================================
This package includes tools for calculating a variety of galaxy cluster properties, as well as mass-richness and mass-concentration scaling relations, and weak lensing profiles. These include surface mass density (Sigma) and differential surface mass density (DeltaSigma) for NFW halos, both with and without the effects of cluster miscentering.
For more information, visit http://clusterlensing.readthedocs.org/
"""
NAME = "clusterlensing"
AUTHOR = "Jes Ford"
AUTHOR_EMAIL = "jesford@uw.edu"
MAINTAINER = "Jes Ford"
MAINTAINER_EMAIL = "jesford@uw.edu"
URL = 'http://github.com/jesford/clusterlensing'
DOWNLOAD_URL = 'http://github.com/jesford/clusterlensing'
LICENSE = 'MIT'
VERSION = '0.1.0'

setup(name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    license=LICENSE,
    packages=['clusterlensing'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
        ],
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "astropy"
        ]
     )