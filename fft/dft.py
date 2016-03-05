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

def dft(signal):
    """
    Discrete fourier transformations
    """
    signal = np.asarray(signal, dtype=float)
    N = signal.shape[0]

    # Make sure we have enough points
    if N < 1:
        raise ValueError("Invalid number of FFT data points (%d) specified." % N)

    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * pi * k * n / N)
    return np.dot(M, signal)

def idft():
    """
    Inverse discrete fourier transformations
    """
    pass
