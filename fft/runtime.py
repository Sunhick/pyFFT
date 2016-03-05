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

def plot(data):
    x = data.keys()
    y = data.values()
    
    plt.figure()
    m = plt.scatter(x, y, color='b', alpha=.5)
    plt.xlim(0, max(x))
    plt.ylim(0, max(y))

    plt.xlabel('N')
    plt.ylabel('time')
    plt.title("runtime of FFT")
    
    plt.savefig('runtime.png')
    plt.show()

def serialize(data):
    import pickle
    out = open('data.pkl', 'wb')
    pickle.dump(data, out)
    out.close()

def main(start, end, step):
    data = {}
    for n in range(start, end+1, step):
        print 'Running for ', n, n
        #n = math.pow(2, n)
        x = np.random.random(n)
        # timer = timeit.Timer(lambda: fft.fft(x))
        timer = timeit.Timer(lambda: dft.dft(x))
        data[n] = timer.timeit(number=1)

    serialize(data)
    plot(data)

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
    main(args.start, args.end, args.step)
