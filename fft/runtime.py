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

def main(*argv):
    data = {}
    N = [i for i in np.arange(1, 5000, 5)]

    for n in N:
        print 'Running for ', n, n
        #n = math.pow(2, n)
        x = np.random.random(n)
        # timer = timeit.Timer(lambda: fft.fft(x))
        timer = timeit.Timer(lambda: dft.dft(x))
        data[n] = timer.timeit(number=1)

    serialize(data)
    plot(data)

if __name__ == '__main__':
    main(sys.argv)
