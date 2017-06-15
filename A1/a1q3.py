# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:37:42 2017

@author: Ming
"""

s = 'bjhgzxoyveadimecdxnmko'
lengthCount = 0; maxCount = 0; initialIndex = 0
for i in range(0, len(s) - 1): 
    if s[i] <= s[i+1]:
            lengthCount += 1
    else:
        if lengthCount > maxCount:
                maxCount = lengthCount
                initialIndex = i - maxCount
        lengthCount = 0
    if i == len(s) - 2: 
        if lengthCount > maxCount:
                maxCount = lengthCount
                initialIndex = i - maxCount + 1

            
print("Longest substring in alphabetical order is: " + s[initialIndex: maxCount + initialIndex + 1])