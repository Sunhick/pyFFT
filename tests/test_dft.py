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

    def test_dft(self):
        x = np.random.random(1024)
        assert(np.allclose(fft.dft(x), np.fft.fft(x), True))

def main(*argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
