import random


def ballTaker():
    if float(3)/7 >= random.random():

        if (float(2))/6 >= random.random():
            return "succes"
        
        else:
            return "fail"
    
    else:
        return "fail"

results = []

def Experiment(NumTrials):
    for i in range(0, NumTrials):
        
        if ballTaker() == "succes":
            results.append("succes")
        
        else: 
            continue

    return float(len(results))/NumTrials


print Experiment(10000000)
