# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:12:05 2017

@author: Ming
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    for i in range(0, len(aTup), 2):
        newTup += (aTup[i],)
    return newTup
print(oddTuples((2, 3)))


def oddTuples2(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]

print (oddTuples((7,2,3,5)))