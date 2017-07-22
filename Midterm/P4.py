#Problem 7
#Write a function called dict_invert that takes in a dictionary with immutable values
#and returns the inverse of the dictionary. 
#The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. 
#The value for a key in the inverse dictionary is a sorted list (increasing order) 
#of all keys in d that have the same value in d.

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    invert_d = {}
    for m, n in d.items():          
        if n not in invert_d: 
            invert_d[n] = []
        invert_d[n].append(m)
        invert_d[n].sort()
    return invert_d
        
print(dict_invert({4:True, 2:True, 0:True}))