#!/usr/bin/python
from __future__ import division, print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#read data
X, Y = np.loadtxt('A12_data.dat', unpack=True)
ye = .2

#really, do I have to scipy.curvefit this? linregress would suffice as well
def poly(x, a=.0, b=.0):
	return(a*x + b)

#fit
par, cov = curve_fit(poly, X, Y, sigma=[ye for i in range(len(X))], absolute_sigma=True)

#perform chi^2 test
chi2 = np.sum((Y - poly(X, par[0], par[1]))**2 / poly(X, par[0], par[1]))

#plot all the things
X_lin = np.linspace(X[0], X[-1], 1000)
plt.errorbar(X, Y, yerr=ye, fmt='o', label='data')
plt.plot(X_lin, poly(X_lin, par[0], par[1]), label='fit: $y(x)=a\\cdot x + b$\n$a=%.2f, b=%.2f$\n$\\chi^2 = %.2f$' %(par[0], par[1], chi2))
plt.grid()
plt.legend()
plt.show()
