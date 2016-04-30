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

from scipy.interpolate import interp1d
from scipy.interpolate import InterpolatedUnivariateSpline

def logplot(ind, fft, filename):
    x = ind
    y = fft

    y = [math.log(i, 2) for i in y]

    plt.figure()
    m = plt.scatter(x, y, color='b', alpha=.5)
    #plt.yscale('log')
    #plt.xscale('log')
    plt.xlabel('N')
    plt.ylabel('time')
    plt.title("runtime of FFT in logscale")
    
    plt.savefig(filename)
    plt.show()

def plot(x, dft, fft, filename):
    x = np.array(x)
    y = np.array(dft)
    y1 = np.array(fft)

    #edft = interp1d(x, y, kind='quadratic')
    #efft = interp1d(x, y1, kind='slinear')
    
    plt.figure()

    # scatter plot
    # m = plt.scatter(x, y, color='b', alpha=.5)
    # n = plt.scatter(x, y1, color='r', alpha=.5)
    # plt.legend((m, n),('dft', 'fft'), loc='upper left')
    # plt.xlim(0, max(x))
    # plt.ylim(0, max(y+y1))

    xnew = np.linspace(x[0], x[-1], num=len(x)*2, endpoint=True)

    # DFT
    c1 = .00000009
    c2 = .00000004
    gn = x**2
    #plt.plot(x,y, '-', x, c1*gn, '-', x, c2*gn, '-')
    plt.semilogx(x,y, '.', x, c1*gn, '.', x, c2*gn, '.')

    # FFT
    #c1 = .0000003
    #c2 = .00000019
    #gn = np.array([i*np.log(i) for i in x])
    #plt.plot(x,y1, '-', x, c1*gn, '-', x, c2*gn, '-')
    #plt.semilogx(x,y1, '-', x, c1*gn, '-', x, c2*gn, '-')

    #plt.plot(x, y, 'o', x, y1, 'o', xnew, edft(xnew), '-', xnew, efft(xnew), '-')

    plt.xlabel('N')
    plt.ylabel('time')
    plt.title("runtime of FFT")
    #plt.title("runtime of DFT")
    plt.xlim(xmin=1)
    plt.xlim(xmin=1)
    plt.legend(['dft', 'c1*n^2', 'c2*n^2'], loc='best')
    #plt.legend(['fft', 'c1*nlog(n)', 'c2*nlog(n)'], loc='best')
    
    plt.savefig(filename)
    plt.show()

def serialize(data, fn):
    import pickle
    out = open(fn, 'wb')
    pickle.dump(data, out)
    out.close()

def main(start, end, step, filename):
    rt_dft = []
    rt_fft = []
    rt_ran = []
    for n in range(start, end+1, step):
        print 'Running for ', n#, math.pow(2, n)
        #n = math.pow(2, n)
        x = np.random.random(n)
        #fft_timer = timeit.Timer(lambda: fft.fft(x))
        dft_timer = timeit.Timer(lambda: dft.dft(x))

        rt_ran.append(n)
        rt_dft.append(dft_timer.timeit(number=1))
        #rt_fft.append(fft_timer.timeit(number=1))

    # serialize(rt_dft, 'dft.pkl')
    # serialize(rt_fft, 'fft.pkl')
    # serialize(rt_ran, 'xrange.pkl')
    #print 'len: ', len(rt_fft)
    # extrapolation the data for fft and dft before plot
    # so we have more points to plot
    #rt_ran, rt_dft, rt_fft = Extrapolation(rt_ran, rt_dft, rt_fft, end, end+20, step)
    #print 'done extrapolating.... len:', len(rt_fft)
    plot(rt_ran, rt_dft, rt_fft, filename)
    #logplot(rt_ran, rt_fft, 'fft_logscale.png')

def Extrapolation(rind, rdft, rfft, start, end, step):
    exp_x = np.array([math.pow(2, i) for i in range(start, end+1, step)])
    # spline order: 1 linear, 2 quadratic, 3 cubic ... 
    # do inter/extrapolation
    dft_exp = InterpolatedUnivariateSpline(rind, rdft, k=2)
    fft_exp = InterpolatedUnivariateSpline(rind, rfft, k=1)

    dft_y = dft_exp(exp_x)
    fft_y = fft_exp(exp_x)

    for key, dft_val, fft_val in zip(exp_x, dft_y, fft_y):
        rdft.append(dft_val)
        rfft.append(fft_val)
        rind.append(key)

    return rind, rdft, rfft

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
