# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3c import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(steps, numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    exp1 = simulationWithDrug(100, 1000, 0.1, 0.05, {"guttagonol" : False}, 0.005, numTrials, steps)

    print exp1 
    pylab.hist(exp1, bins=range(0, 501), histtype='bar')
    pylab.title("%s steps" % steps) 
    pylab.xlabel("number of viruses")
    pylab.show()
    

simulationDelayedTreatment(0, 100)

simulationDelayedTreatment(75, 100)

simulationDelayedTreatment(150, 100)

simulationDelayedTreatment(300, 100)


# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
