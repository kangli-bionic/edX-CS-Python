# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = 'a test string'
vowel = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel += 1
print("Number of vowels: " + str(vowel))
