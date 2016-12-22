import random

def balls(NumTrials):
	succes = 0.0
	
	for i in range(NumTrials):
		# print random.random()

		if random.random() < float(1)/2:
			
			if random.random() < float(2)/5:
				
				if random.random() < float(1)/4:
					succes += 1
					print succes

				else:
					continue

			else: 
				continue
		else:
			continue

	return float(succes)/NumTrials

print balls(100000)


