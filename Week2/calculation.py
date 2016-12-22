import numpy as np

new_list = range(0, 366)
reverse_list = new_list[::-1]

p = float(1)

def findN(p):
	i = 0 
	while(1-p) < 0.99:
		p = p*float(reverse_list[i])/365
		i += 1
	return i-1

print findN(p)





