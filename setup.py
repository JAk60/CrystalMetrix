# setup.py
from setuptools import setup
from Cython.Build import cythonize
import numpy as np
import os

# Set compiler to use MinGW
os.environ['CC'] = 'gcc'
os.environ['CXX'] = 'g++'

setup(
    ext_modules=cythonize("permanent.pyx"),
    include_dirs=[np.get_include()],
)
