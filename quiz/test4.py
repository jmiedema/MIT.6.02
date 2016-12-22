import random, pylab
from collections import Counter
import operator 

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)

    pylab.show()

    
                    
# Implement this -- Coding Part 2 of 2


# makeHistogram([random.random()*100 for x in range(0,10000)], 10, "values", "quanity", title=None)

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    
    final_list = []

    for i in range(numTrials):
        temp_result = []
        for n in range(numRolls):
            temp_result.append(die.roll())

        final_result = Counter(temp_result)
        key = max(final_result.iteritems(), key=operator.itemgetter(1))[0]
        print final_result

        final_list.append(final_list[key])

    return sum(float(final_list))/numTrials

    
# One test case
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)













