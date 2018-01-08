#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

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

""" Exercise 1 """
if len(sys.argv) != 2:
	quit('Usage: ./08 - montecarlo.py <a|b|c>')

# a)
if sys.argv[1] == 'a':
	X = np.linspace(-1, 1, 1000)
	rands, ntrials = acc_rej(scattering_dist, N, -1., 1.)

	fig, ax = plt.subplots()

	ax.hist(rands, bins=bin_size, normed=1, histtype='step')
	ax.plot(X, scattering_dist(X))
	ax.set_xlabel('$x$')
	ax.set_ylabel('occurences')
	ax.grid()

	plt.savefig('scattering_dist.pdf')

elif sys.argv[1] == 'b':
	pass

elif sys.argv[1] == 'c':
	pass
