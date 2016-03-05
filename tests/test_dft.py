#!/usr/bin/python

"""
test_dft.py

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

class TestDFT(unittest.TestCase):
    """
    Test discrete fourier transformations
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_dft(self):
        x = np.random.random(1024)
        self.assertTrue(np.allclose(fft.dft(x), np.fft.fft(x)))

    def test_invalid_points_dft(self):
        x = []
        self.assertRaises(ValueError, fft.dft, x)

    def test_long_dft(self):
        x = np.random.random(1020)
        self.assertTrue(np.allclose(fft.dft(x), np.fft.fft(x)))

    def test_smal_odd_dft(self):
        x = np.random.random(103)
        self.assertTrue(np.allclose(fft.dft(x), np.fft.fft(x)))

def main(*argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
