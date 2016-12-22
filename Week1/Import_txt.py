# This script plot data from input file 

import pylab as plt
import numpy as np


def Inputfunction(input_file):
	high = []
	low = []

	with open(input_file, 'r') as input_file:
		for line in input_file:
			if line[0].isdigit():
				high.append(int(line.strip().split(" ")[1]))
				low.append(int(line.strip().split(" ")[2]))
		input_file.close()
	return (high, low)


def ProducePlot(highTemps, lowTemps):
	diffTemps = np.subtract(highTemps, lowTemps)
	plt.title('Day by Day Ranges in Temperature in Boston in July 2012')
	plt.xlabel('Days')
	plt.ylabel('Temp difference')
	plt.plot(range(1,32), diffTemps)
	plt.show()


# initiate graphs
ProducePlot(Inputfunction("JulyTemp.txt")[0], Inputfunction("JulyTemp.txt")[1])







