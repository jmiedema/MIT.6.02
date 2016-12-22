# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab
import itertools
''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self. maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        if random.random() <= self.getClearProb():
            return True
        else:
            return False
        

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        virus_odds = random.random()
        
        if virus_odds <= (self.maxBirthProb * (1 - popDensity)):
            new_instance = SimpleVirus(self.maxBirthProb, self.clearProb)
            return new_instance
        else: 
            raise NoChildException()



# Virus1 = SimpleVirus(0.5, 0.5)
# print Virus1.reproduce(0.2)



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """

        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.getViruses())


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        popDensity = (float(self.getTotalPop())/self.getMaxPop())
        temp_viruses = []

        for virus in self.viruses:
            if virus.doesClear() == True:
                self.viruses.remove(virus)

            else: 
                try: 
                    temp_virus = virus.reproduce(popDensity)
                    temp_viruses.append(temp_virus)
                except NoChildException: 
                    continue

        for temp_virus in temp_viruses:
            self.viruses.append(temp_virus)

#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    
    virus_growth_list = []

    # iterate for number of trials
    for trial in range(numTrials):

        if (trial+1) % 5 == 0:
            print "%i trials have been conducted" % (trial+1)
        
        virus_growth = []
        # create new patient
        new_patient = Patient([SimpleVirus(maxBirthProb, clearProb) for x in range(0, numViruses)], maxPop)

        # iterate through 300 time steps
        for t in range (0, 300):
            new_patient.update()
            virus_growth.append(len(new_patient.viruses))

        # append to virus list
        virus_growth_list.append(virus_growth)

    # sum timestaps and find average
    final_list = [sum(x)/numTrials for x in zip(*virus_growth_list)]

    return final_list


# simulation_list = simulationWithoutDrug(100, 1000, .1, .05, 100)
# pylab.plot(range(0, 300), simulation_list)
# pylab.show()


#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb


    def isResistantTo(self, key):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if key in self.resistances:
            if self.resistances[key] == True:
                return True
            else:
                return False
        else: 
            return False


    def isResistantTolist(self, activeDrugs):

        
        for key in activeDrugs:
            if self.isResistantTo(key) == True:
                continue
            else:
                return False

        return True

    


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # parent is resistent to all drugs that are used
        if self.isResistantTolist(activeDrugs) == True:
            
            # chance of reproduction
            reproduction_chance = random.random()

            # will reproduce
            if reproduction_chance <= (self.maxBirthProb * (1 - popDensity)):
                
                # dict for new particle
                temp_dict = {}

                # check each drug of parent
                for key in self.resistances:
                    
                    # parent is resistent
                    if self.isResistantTo(key) == True:
                    
                        # chance of inheritance
                        inheritance_chance = random.random()
                        
                        # virus inherits
                        if inheritance_chance <= (1-self.mutProb):

                            # virus inherits
                            temp_dict[key] = True
                        
                        # virus does not inherit
                        else: 
                            temp_dict[key] = False

                    # parent is not resistent
                    else: 

                        # chance of generating enheritance
                        resistance_chance = random.random()
                        
                        # child generates inheritance
                        if resistance_chance <= self.mutProb:
                            temp_dict[key] = True

                        # child fails to generate inheritance
                        else:
                            temp_dict[key] = False

                # child is produced
                new_instance = ResistantVirus(self.maxBirthProb, self.clearProb, temp_dict, self.mutProb)
                return new_instance



            # will not reproduce
            else:
                
                # child is not produced
                raise NoChildException("bad reproduction odds")


        else:

            #child is not produced
            raise NoChildException("drug kills parent")


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses 
        self.maxPop = maxPop
        self.activeDrugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        self.activeDrugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.activeDrugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        counter = 0

        for virus in self.viruses:
            for drug in drugResist:
                if virus.isResistantTo(drug) == True:
                    continue
                else: 
                    break
                counter += 1

        return counter


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        popDensity = float(len(self.viruses))/self.maxPop

        temp_virus_list = []

        for virus in self.viruses:

            # chance of a particle not surviving
            survival_chance = random.random()

            # particle dies
            if survival_chance <= virus.clearProb:
                self.viruses.remove(virus)

            # particle survives and might reproduce
            else: 

                # particle reproduces
                try:
                    temp_virus = virus.reproduce( popDensity, self.activeDrugs)
                    temp_virus_list.append(temp_virus)

                # particle fails to reproduce
                except NoChildException:
                    continue

        # append new viruses to existing viruses
        for virus in temp_virus_list:
            self.viruses.append(virus)

        # return number of viruses
        return len(self.viruses)


# virus_list = [ResistantVirus(0.1, 0.05, {"guttagonol" : False}, 0.005) for x in range(0,100)]
# new_patient = TreatedPatient(virus_list, 1000)

# for n in range(0, 300):
#     new_patient.update()
#     print len(new_patient.viruses)
#     # for virus in new_patient.viruses:
#     #     print virus.resistances




#
# PROBLEM 5
#

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, Experiment):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    virus_list = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for x in range(0, numViruses)]

    
    final_result = []

    for i in range (numTrials):

        if (i+1) % 10 == 0:
            print "%i trials have been conducted" % (i+1)

        temp_result = []
        new_patient = TreatedPatient(virus_list, maxPop)

        for t in range(0, Experiment):
            new_patient.update()
            temp_result.append(len(new_patient.viruses))


        new_patient.addPrescription("guttagonol")

        for t in range(Experiment, (Experiment+150)):
            new_patient.update()
            temp_result.append(len(new_patient.viruses))

        print temp_result[Experiment+149]
        final_result.append(temp_result[Experiment+149])

    return final_result

    



# y_axis = simulationWithDrug(100, 1000, 0.1, 0.05, {"guttagonol" : False}, 0.005, 100)

# pylab.plot(range(0,300), y_axis)
# pylab.show()


    

# print simulationWithDrug(100, 1000, 0.1, 0.05, {"guttagonol" : False}, 0.05, 1)




