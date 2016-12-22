import math

new_input = [10, 4, 12, 15, 20, 5]

mean = sum(new_input)/len(new_input)

def stdcalc(mean, new_input):
	variance = float(0)
	for i in new_input:
		variance += float(i-mean)**2
	
	return math.sqrt(variance/len(new_input))

sdev = stdcalc(mean, new_input)
sdevco = sdev/mean

print sdev, sdevco





