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

from scipy.interpolate import InterpolatedUnivariateSpline

def plot(dft, fft, filename):
    x = dft.keys()
    y = dft.values()

    y1 = fft.values()
    
    plt.figure()
    m = plt.scatter(x, y, color='b', alpha=.5)
    n = plt.scatter(x, y1, color='r', alpha=.5)
    # plt.xlim(0, max(x))
    # plt.ylim(0, max(y+y1))

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
    rt_dft = {}
    rt_fft = {}
    for n in range(start, end+1, step):
        print 'Running for ', n, math.pow(2, n)
        n = math.pow(2, n)
        x = np.random.random(n)
        fft_timer = timeit.Timer(lambda: fft.fft(x))
        dft_timer = timeit.Timer(lambda: dft.dft(x))
        rt_dft[n] = dft_timer.timeit(number=1)
        rt_fft[n] = fft_timer.timeit(number=1)

    serialize(rt_dft, 'dft.pkl')
    serialize(rt_fft, 'fft.pkl')
    print 'len: ', len(rt_fft)
    # extrapolation the data for fft and dft before plot
    # so we have more points to plot
    rt_dft, rt_fft = Extrapolation(rt_dft, rt_fft, end, end+20, step)
    print 'done extrapolating.... len:', len(rt_fft)
    plot(rt_dft, rt_fft, filename)

def Extrapolation(rdft, rfft, start, end, step):
    exp_x = np.array([math.pow(2, i) for i in range(start, end+1, step)])
    # spline order: 1 linear, 2 quadratic, 3 cubic ... 
    # do inter/extrapolation
    dft_exp = InterpolatedUnivariateSpline(rdft.keys(), rdft.values(), k=2)
    fft_exp = InterpolatedUnivariateSpline(rfft.keys(), rfft.values(), k=1.5)

    dft_y = dft_exp(exp_x)
    fft_y = fft_exp(exp_x)

    for key, dft_val, fft_val in zip(exp_x, dft_y, fft_y):
        rdft[key] = dft_val
        rfft[key] = fft_val

    return rdft, rfft

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
