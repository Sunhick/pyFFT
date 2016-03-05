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

def fft(signal):
    """
    Fast fourier transformations
    """
    signal = np.asarray(signal, dtype=float)
    N = signal.shape[0]

    # Make sure we have enough points
    if N < 1:
        raise ValueError("Invalid number of FFT data points (%d) specified." % N)

    # fft works only with even length
    if N % 2 > 0:
        # When it's even fallback to DFT
        # retun dft.dft(signal)
        raise ValueError("size of input must be a power of 2")

    if N <= 32: # threshold point for fft
        return dft.dft(signal)

    xeven = fft(signal[::2])
    xodd = fft(signal[1::2])
    fac = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([xeven + fac[:N / 2] * xodd,
                           xeven + fac[N / 2:] * xodd])

def FFT_vectorized(signal):
    """A vectorized, non-recursive version of the Cooley-Tukey FFT"""
    signal = np.asarray(signal, dtype=float)
    N = signal.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("size of signal must be a power of 2")

    # N_min here is equivalent to the stopping condition above,
    # and should be a power of 2
    N_min = min(N, 32)
    
    # Perform an O[N^2] DFT on all length-N_min sub-problems at once
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, signal.reshape((N_min, -1)))

    # build-up each level of the recursive calculation all at once
    while X.shape[0] < N:
        X_even = X[:, :X.shape[1] / 2]
        X_odd = X[:, X.shape[1] / 2:]
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()

def ifft(signal):
    """
    Inverse Fast fourier transformations
    """
    tsignal = fft([t.conjugate() for t in signal])
    return [t.conjugate()/len(signal) for t in tsignal]
