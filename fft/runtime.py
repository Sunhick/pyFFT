#!/usr/bin/python

"""
runtime.py

Generate the runtime scatter plot for FFT
"""

__author__ = "Sunil"
__copyright__ = "Copyright 2015"
__license__ = "GNU License"
__version__ = "0.1.0"
__email__ = "suba5417@colorado.edu"

import sys
import fft
import dft
import math
import timeit
import argparse
import numpy as np
import matplotlib.pyplot as plt

def plot(dft, fft, filename):
    x = dft.keys()
    y = dft.values()

    y1 = fft.values()
    
    plt.figure()
    m = plt.scatter(x, y, color='b', alpha=.5)
    n = plt.scatter(x, y1, color='r', alpha=.5)
    plt.xlim(0, max(x))
    plt.ylim(0, max(y+y1))

    plt.xlabel('N')
    plt.ylabel('time')
    plt.title("runtime of FFT & DFT")
    plt.legend((m, n),('dft', 'fft'), loc='lower right')
    
    plt.savefig(filename)
    plt.show()

def serialize(data, fn):
    import pickle
    out = open(fn, 'wb')
    pickle.dump(data, out)
    out.close()

def main(start, end, step, filename):
    dft = {}
    fft = {}
    for n in range(start, end+1, step):
        print 'Running for ', n, math.pow(2, n)
        n = math.pow(2, n)
        x = np.random.random(n)
        fft_timer = timeit.Timer(lambda: fft.fft(x))
        dft_timer = timeit.Timer(lambda: dft.dft(x))
        dft[n] = dft_timer.timeit(number=1)
        fft[n] = fft_timer.timeit(number=1)

    serialize(dft, 'dft.pkl')
    serialize(fft, 'fft.pkl')
    plot(dft, fft, filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FFT/DFT runtime')
    parser.add_argument("-start", type=int,
                        help="starting range",
                        required=True)
    parser.add_argument("-end", type=int,
                        help="ending range",
                        required=True)
    parser.add_argument("-step", type=int, default=1,
                        help="step size for FFT/DFT",
                        required=False)
    parser.add_argument("-save", type=str, default="runtime.png",
                        help="file name to save the plot",
                        required=False)
    args = parser.parse_args()
    main(args.start, args.end, args.step, args.save)
