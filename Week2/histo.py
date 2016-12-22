import random
import pylab

values = []

for i in range(100000):
	num = random.random()
	values.append(num)

pylab.hist(values, bins=11)
pylab.show()