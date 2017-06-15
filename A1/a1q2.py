# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:29:08 2017

@author: Ming
"""
s = 'azcbobobegghakl'
bobCount = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob': 
        bobCount += 1
print("Number of times bob occurs is: " + str(bobCount))