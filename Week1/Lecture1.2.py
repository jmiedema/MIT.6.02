import pylab
import math

x_values = [x for x in range(-1000, 1000)]
y_values = [x**2 for x in range(-1000, 1000)]

pylab.plot(x_values, y_values)
pylab.show()