#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from scipy import stats
import timeit as time

N = 10000

s = np.array([np.loadtxt('sample1.dat'), np.loadtxt('sample2.dat')])

def d(s):

	means = [np.mean(x) for x in s]
	stds  = [np.std(x) for x in s]

	sigma = np.sqrt(stds[0]**2 / len(s[0]) + stds[1]**2 / len(s[1]))

	return np.abs(means[0]-means[1])/sigma

union = np.concatenate(s)
S1_primes = []
S2_primes = []

start = time.default_timer()	#time-critical point start
for i in range(N):

	S1 = [np.random.choice(union) for x in range(len(s[0]))]
	S2 = [np.random.choice(union) for x in range(len(s[1]))]
	S1_primes.append(S1)
	S2_primes.append(S2)

dvalues = [d([S1_primes[i], S2_primes[i]]) for i in range(N)]
d_obs = d(s)

counter = 0
for i in range(N):
	if dvalues[i] > d_obs:
		counter += 1

stop = time.default_timer()	#time-critical point end

ratio = (N - counter) / N

print('\nFinished job. Time required: %.2fs\nd_obs = %.2f\nnumber of times, d_obs > d_sampled = %i\nratio (N - counts) / N: %.2f\n' %((stop-start), d_obs, counter, ratio))
