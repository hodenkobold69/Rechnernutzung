#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import os
import sys
from matplotlib import cm

if len(sys.argv) != 2:
	quit('Usage: ./09-poissonlikelihood.py <show|save>')

""" fields, constants """
data = np.asarray([2,6,6,4,8,3,2,4,4])
N = len(data)

""" functions """
def fPoisson(x, lamb):
	k=np.round(x)
	return (lamb**k)/np.exp(lamb)/sp.gamma(k+1.)


def negLogL(lamb, dist, x):
	return -np.sum(np.log(dist(x,lamb)))

""" main program """
for i in range(N):

	sliced = np.asarray(data[:i+1])
	lamb = np.linspace(.1,10,1000)
	negLog = [negLogL(i, fPoisson, sliced) for i in lamb]

	doublerainbowmofo = (float(i)+1) / N
	plt.semilogy(lamb,negLog,c=cm.jet(doublerainbowmofo),label=("n = %i"%(i+1)))

""" plot stuff """
plt.xlabel('$\lambda$')
plt.ylabel('log$_{10}(nl\cal{L}(\lambda)$)')
plt.grid()
plt.legend()

""" save or show """
if sys.argv[1] == 'show':
	min_index = np.argmin(negLog)
	print('\nMinimum at %.3f'%negLog[min_index])
	print('classical mean: %.3f' %np.mean(data))
	print('my mean: %.3f' %lamb[min_index])
	plt.show()
elif sys.argv[1] == 'save':
	min_index = np.argmin(negLog)
	print('\nMinimum at %.3f'%negLog[min_index])
	print('classical mean: %.3f' %np.mean(data))
	print('my mean: %.3f' %lamb[min_index])
	plt.savefig(__file__[:-2] + 'pdf')
else:
	quit('You effed it up. Try again.')
