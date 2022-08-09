import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Panda3_direct_tooltip",#module name
    version = "0.1",
    author = "Bruno Maximilian Voß",
    author_email = "bruno.m.voss@gmail.com",
    description = ("creates a tooltip in panda3d with panda3d"),
    
    license = "BSD 2-Clause License",
    keywords = "panda3d",
   
    packages=['DirectTooltip'],#foldername
    
)
