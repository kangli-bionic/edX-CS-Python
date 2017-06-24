# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:35:25 2017

@author: Ming
"""

balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
fixedMonthlyPayment = 0
checking = True
def isFixedPayment (balance, monthlyInterestRate, fixedMonthlyPayment):
    updatedBalance = balance
    month = 0
    while month < 12: 
        monthlyUnpaid = updatedBalance - fixedMonthlyPayment
        updatedBalance = monthlyUnpaid + monthlyUnpaid*monthlyInterestRate
        month += 1
    if updatedBalance > 0:
        return False
    else:
        return True
while checking:
    if isFixedPayment(balance, monthlyInterestRate, fixedMonthlyPayment):
        break
    else: 
        fixedMonthlyPayment += 10
print('Lowest payment: ' + str(fixedMonthlyPayment))        



    