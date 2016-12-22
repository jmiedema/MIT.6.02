# generate all combinations of N items

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    total = []

    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            # test bit jth of integer i
            print "moving %i %i to the right gives %i" % (i, j, (i >>j))
            if (i >> j) % 2 == 1:
                bag1.append(items[j])
                print "added"
            else: 
                bag2.append(items[j])


        total.append((bag1, bag2))
    
    return total

items = ["box", "chair"]

total = powerSet(items)

print total



def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """

