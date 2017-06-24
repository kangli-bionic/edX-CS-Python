# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 18:07:52 2017

@author: Ming
"""

balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12.0
lowerBound = balance/12.0
upperBound = (balance*(1 + monthlyInterestRate)**12)/12.0
monthlyPayment= (lowerBound + upperBound)/2
def check (balance, monthlyInterest, monthlyPayment):
    updatedBalance = balance
    month = 0
    while month < 12 :
         monthlyUnpaid = updatedBalance - monthlyPayment
         updatedBalance = monthlyUnpaid + monthlyUnpaid*monthlyInterestRate
         month += 1
    return updatedBalance
    
while True:
    if check(balance, monthlyInterestRate, monthlyPayment) > 0.005:
        lowerBound = monthlyPayment
    elif check(balance, monthlyInterestRate, monthlyPayment) < -0.005:
        upperBound = monthlyPayment
    else:
        break
    monthlyPayment = (lowerBound + upperBound)/2 
print('Lowest Payment: ' + str(round(monthlyPayment, 2)))

