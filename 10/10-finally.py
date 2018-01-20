#!/usr/bin/python3

############# NOTE #########################
# Template was shit, this is how to do it  #
# correctly. #nohate, of course            #
############################################

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

if len(sys.argv) != 2:
	quit('Usage: ./10-finally.py <a|b|c|d>')

""" Fields, constants """
Nsig = 50000
max_x = 10
signal = np.zeros(Nsig)
dTsig = 1
dTn = 10*dTsig
t = 0

#exponential curve
X_lin = np.linspace(0, max_x, 1000)
Y = np.exp(-X_lin)

for i in range(Nsig):

	t += np.random.exponential(dTsig)
	signal[i] = t

dT = signal[1:] - signal[:-1]

if sys.argv[1] == 'a':

	N = 500

	plt.plot(X_lin, Y, label='expectation')

	plt.hist(dT, N, normed=1, range=(0, max_x), label='occurences')
	plt.legend()
	plt.show()
	quit('That\'s all folks.')

noise = []
tn = signal[0]

while True:

	tn += np.random.exponential(dTn)

	if tn > signal[-1]:
		break

	noise.append(tn)

noise = np.array(noise)
data = np.sort(np.append(signal, noise))

dTdata = data[1:] - data[:-1]

if sys.argv[1] == 'b':

	N = 500

	plt.hist(dTdata, N, normed=1, range=(0, max_x), label='waiting time n + s')
	plt.hist(dT, N, normed=1, range=(0, max_x), label='waiting time s',alpha=0.3)
	plt.plot(X_lin, Y, label='expectation s')
	plt.plot(X_lin, Y + np.exp(-X_lin * 10) / 10, label='expectation n + s')
	plt.legend()
	plt.show()
	quit('That\'s all folks.')

if sys.argv[1] == 'c':

	N = 500
	plt.hist(signal, N, label='signal')
	plt.hist(noise, N, label='noise')
	plt.legend()
	plt.show()
	quit('That\'s all folks.')

if sys.argv[1] == 'd':

	N = 500
	data_bins, stuff, morestuff = plt.hist(data, N, range=(0, signal[-1]))
	plt.clf()
	plt.hist(data_bins, 100, normed=1, label='bin contents')
	X = np.arange(70, 150)
	plt.plot(X, 1.9*ss.poisson.pmf(X, Nsig * 1.1 / N), label='expectation')
	plt.legend()
	plt.show()
	quit('That\'s all folks.')

if sys.argv[1] == 'e':

	N = 500
	events = [-100]

	for t in data:

		d = t - events[-1]

		if d > 0.2 or np.random.random() < 5 * d:

			events.append(t)
			continue

	events = np.array(events[1:])


	event_bins, stuff, morestuff = plt.hist(events, N, range=(0, signal[-1]))
	plt.clf()
	plt.hist(event_bins, 100, normed=1, label='bin contents')

	X = np.arange(70, 150)
	plt.plot(X, 1.9*ss.poisson.pmf(X, Nsig * 1.1 / N), label='expectation')

	rate = len(events) / len(signal)

	print('actual rate: %.1f, observed rate: %.3f, ratio: %.3f' %(1.1, rate, 1.1/rate))

	plt.legend()
	plt.show()
	quit('That\'s all folks.')
