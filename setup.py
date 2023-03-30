from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Download Siddhesh Kulthe\'s Profile!'
LONG_DESCRIPTION = 'A package that downloads Siddhesh Kulthe\'s Resume on your computer.'

# Setting up
setup(
    name="sid-profile",
    version=VERSION,
    author="Siddhesh Kulthe",
    author_email="<siddheshkulthe43@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[''],
    keywords=['python', 'resume', 'sid', 'siddhesh kulthe', 'profile', 'CV'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers, Recruiters",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)