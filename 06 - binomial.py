#!/usr/bin/python
from __future__ import division, print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom

N = 10000 	#number of experiments
n = 10		#number of tosses
p = 0.5		#fair coin
#conduct the coin toss experiment N times with n runs in each experiment
probs = np.zeros(N)
probs = [np.sum(np.around(np.random.rand(n))) for i in range(N)]

#binomial distribution
def B(k, nmax, p):
	return(binom(nmax, k) * p**k * (1-p)**(nmax-k))

#calculate stats
ex = np.mean(probs)
var = np.var(probs)

ex_lit = n*p
var_lit = n*p * (1 - p)

#plot results in histogram
X = np.linspace(0, n, 1000)
plt.hist(probs, range(n+1), normed=True, label='exp.: $\\mu = %.2f, \\sigma^2 = %.2f$' %(ex, var))
plt.plot(X, B(X, n, p), label='theo: $\\mu = %.2f, \\sigma^2 = %.2f$' %(ex_lit, var_lit))
plt.xlabel('number of heads $k$')
plt.ylabel('$H(k)$')
plt.legend()
plt.title('Coin Toss Experiment')
plt.show()
