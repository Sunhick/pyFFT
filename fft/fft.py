#!/usr/bin/python

"""
fft.py

fast fourier transformations
"""

__author__ = "Sunil"
__copyright__ = "Copyright 2015"
__license__ = "GNU License"
__version__ = "0.1.0"
__email__ = "suba5417@colorado.edu"

import dft
import numpy as np

def fft(x):
    """
    Fast fourier transformations
    """
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    # Make sure we have enough points
    if N < 1:
        raise ValueError("Invalid number of FFT data points (%d) specified." % N)

    # fft works only with even length
    if N % 2 > 0:
        # When it's even fallback to DFT
        # retun dft.dft(x)
        raise ValueError("size of input must be a power of 2")
    elif N <= 32: # threshold for fft
        return dft.dft(x)
    else:
        xeven = fft(x[::2])
        xodd = fft(x[1::2])
        fac = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([xeven + fac[:N / 2] * xodd,
                               xeven + fac[N / 2:] * xodd])
