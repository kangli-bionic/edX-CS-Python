# Problem 9
#We define a permutation as follows:
#the lists have the same number of elements
#list elements appear the same number of times in both lists

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if not L1 and not L2:
        return (None, None, None)
    if len(L1) != len(L2):
        return False
    else:
        for i in L1:
            if L1.count(i) != L2.count(i):
                return False
    freqEl = max(set(L1), key=L1.count)  #set removes duplicates, key counts frequency in L1
    freq = L1.count(freqEl)
    return (freqEl, freq, type(freqEl))

#   largest = [0, 0]
#   for i in L1:
#      if L1.count(i) > largest[1]: 
#           largest[1] = L1.count(i)
#           largest[0] = i
#   return (largest[0], largest[1], type(largest[0]))

print(is_list_permutation([1, 2, '5', 2, 5, 3, 4, 4, 5, 5, 6], [3, 5, 1, '5', 2, 5, 2, 6, 4, 5, 4]))
                    
    
