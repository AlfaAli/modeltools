import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "modeltools",
    version = "0.0.1",
    author = "Knut Lisaeter",
    author_email = "knutal@gmail.com",
    description = ("A module for reading and writing hycom files."),
    license = "MIT",
    keywords = "hycom model",
    url = "http://github.com/knutalnersc/modeltools",
    packages=['modeltools','modeltools.hycom','modeltools.cice','modeltools.forcing','modeltools.nemo','tools'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
