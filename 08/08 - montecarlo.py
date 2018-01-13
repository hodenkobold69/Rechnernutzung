#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from scipy import stats
N = 10000	#amount of random numbers to generate
bin_size = 100 #bin size of histograms

def acc_rej(dist, n=10000, xmin=0, xmax=1):

	x = np.linspace(xmin,xmax,1000)
	y = dist(x)
	pmin = 0.
	pmax = y.max()

	# Counters for accepted numbers and trials
	naccept = 0
	ntrial = 0

	rands=[] # output list of random numbers

	while naccept < n:

		x=np.random.uniform(xmin,xmax)
		y=np.random.uniform(pmin,pmax)

		if y < dist(x):

			rands.append(x)
			naccept += 1

		ntrial = ntrial+1

	rands = np.asarray(rands)

	return rands, ntrial

def scattering_dist(x):
	return 3. / 8 * (1 + x**2)

def cauchy_density(x):
	return 1. / np.pi / (1 + x**2)

def cauchy_transformed(x):
	return np.tan(x)

""" Exercise 1 """
if len(sys.argv) != 2:
	quit('Usage: ./08 - montecarlo.py <a|b|c>')

# a)
if sys.argv[1] == 'a':

	X = np.linspace(-1, 1, 1000)
	rands, ntrials = acc_rej(scattering_dist, N, -1., 1.)

	fig, ax = plt.subplots()

	ax.hist(rands, bins=bin_size, normed=1, histtype='step', label='random numbers')
	ax.plot(X, scattering_dist(X), label='$f(x)=\\frac{3}{8}(1 + x^2)$ - distribution')
	ax.set_xlabel('$x$')
	ax.set_ylabel('occurences')
	ax.grid()

	plt.legend()
	plt.savefig('scattering_dist.pdf')

elif sys.argv[1] == 'b':

	rands = [cauchy_transformed(np.random.rand()) for x in range(N)]
	X = np.linspace(0, 1, 1000)

	fig, ax = plt.subplots()

	ax.hist(rands, bins=bin_size, normed=1, histtype='step', label='random numbers')
	ax.plot(X, cauchy_density(X) * np.pi, label='$f(x)=\\frac{1}{\\pi}\\frac{1}{1+x^2}$ - distribution')
	ax.set_xlabel('$x$')
	ax.set_ylabel('occurences')
	ax.set_xlim(0, 1)
	ax.grid()

	plt.legend()
	plt.savefig('cauchy_dist.pdf')

elif sys.argv[1] == 'c':

	data = np.loadtxt('elefant.dat')

	n, bins, patches = plt.hist(data, histtype='step', label='sample data', normed=1)

	bin_centers = bins[:-1] + 0.5 * (bins[1:] - bins[:-1])
	n = np.append(n, 0)
	bin_centers = np.append(bin_centers, 22.)


	""" tried to fit every known distribution to the data --> no distibution was good enough """
	# for cdf in cdfs:
	#
	# 	#fit our data set against every probability distribution
	# 	parameters = eval("scipy.stats."+cdf+".fit(data)")
	#
	# 	#Applying the Kolmogorov-Smirnof one sided test
	# 	D, p = scipy.stats.kstest(data, cdf, args=parameters)
	#
	# 	#pretty-print the results
	# 	print(cdf.ljust(16) + ("p: "+str(p)).ljust(25)+"D: "+str(D))
	#
	# plt.scatter(bin_centers, func(bin_centers, *popt))

	coeff = np.polyfit(bin_centers, n, 6)
	poly = np.poly1d(coeff)

	X = np.linspace(0, bin_centers[-1], 100)
	rands, ntrials = acc_rej(poly, N, 0, max(bins))
	plt.hist(rands, histtype='step', label='generated randoms', normed=1)
	#plt.plot(X, poly(X))

	plt.legend()
	plt.savefig('elefant.pdf')
