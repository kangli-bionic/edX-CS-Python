# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:36:09 2017

@author: Ming
"""

high = 100
low = 0
guess = int((high + low)/2) 
gameOver = False
print ('Please think of a number between 0 and 100!')
while not gameOver:
    print('Is your secret number ' + str(guess) + '?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    while ans != 'c' and ans != 'l' and ans != 'h':
        print('Sorry, I did not understand your input.')
        print('Is your secret number ' + str(guess))   
        ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans == 'c':
        break
    elif ans == 'l':
        low = guess
    else:
        high = guess
    guess = int((high + low)/2)
print('Game over. Your secret number was: ' + str(guess))