#!/usr/bin/python

"""
dft.py

Discrete fourier transformations
"""

__author__ = "Sunil"
__copyright__ = "Copyright 2015"
__license__ = "GNU License"
__version__ = "0.1.0"
__email__ = "suba5417@colorado.edu"

import numpy as np

pi = np.pi

def dft(x):
    """
    Discrete fourier transformations
    """
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * pi * k * n / N)
    return np.dot(M, x)

def idft():
    """
    Inverse discrete fourier transformations
    """
    pass
