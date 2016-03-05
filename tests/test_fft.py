#!/usr/bin/python

"""
test_fft.py

"""

__author__ = "Sunil"
__copyright__ = "Copyright 2015"
__license__ = "GNU License"
__version__ = "0.1.0"
__email__ = "suba5417@colorado.edu"


import fft
import sys
import unittest
import numpy as np

class TestFFT(unittest.TestCase):
    """
    Test Fast fourier transformations
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_fft(self):
        x = np.random.random(1024)
        assert(np.allclose(fft.fft(x), np.fft.fft(x), True))

    def test_small_odd_fft(self):
        x = np.random.random(103)
        self.assertRaises(ValueError, fft.fft, x)

    def test_large_odd_fft(self):
        x = np.random.random(103090987)
        self.assertRaises(ValueError, fft.fft, x)

    def test_long_fft(self):
        x = np.random.random(1020)
        assert(np.allclose(fft.dft(x), np.fft.fft(x), True))

def main(*argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
