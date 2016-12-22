# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.
# Recall that the standard deviation is computed by this equation:

import math

L = ['apples', 'oranges', 'kiwis', 'pineapples']

print [len(x) for x in L]

def stdDevOfLengths(L):
	
	letters = 0
	summed_difs = float(0)

	if len(L) == 0:
		return float('NaN')

	else:
		# find mean
		mean = sum([len(x) for x in L])/len(L)

		#find variance
		for word in L:
			summed_difs = summed_difs + (len(word)-mean)**2
		variance = float(summed_difs/len(L))

		return math.sqrt(variance)


print stdDevOfLengths(L)