# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:12:38 2017

@author: Ming
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr
    if char == aStr[len(aStr)//2]:
        return True
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[:len(aStr)//2])
    else:
        return isIn(char, aStr[len(aStr)//2 +1:])
    return False                           


