#Problem 6

def largest_odd_times(L):
    """ 
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number 
    of times in L. If no such element exists, returns None 
    """
    oddList = []
    for i in L:
        if L.count(i)%2 == 1:   #checks odd number of occurence
            oddList.append(i)
    if not oddList:     #checks if list is empty
        return None
    return max(oddList)

