import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels_proportion = []


    for word in wordList:
        
        vowels = float(0)
        for letter in word:
            print letter
            if letter == "u" or letter == "o" or letter == "a" or letter == "e" or letter == "i":
                vowels += 1
            else: 

                continue
        # print vowels
        vowels_proportion.append(float(vowels/len(word)))

    # print vowels_proportion
    pylab.hist(vowels_proportion, numBins)
    pylab.show()



    

if __name__ == '__main__': 
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
