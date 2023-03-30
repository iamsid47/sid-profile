from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Check out Siddhesh Kulthe\'s profile, or send him a direct message!'
LONG_DESCRIPTION = 'A package that downloads Siddhesh Kulthe\'s Resume on your computer. All you need to do is to import siddhesh and use .Start() method to start the app!'

# Setting up
setup(
    name="siddhesh",
    version=VERSION,
    author="Siddhesh Kulthe",
    author_email="<siddheshkulthe43@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'sid', 'siddhesh kulthe', 'profile', 'message', 'social', 'iamsid47'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)