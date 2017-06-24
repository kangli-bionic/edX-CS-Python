# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:05:30 2017

@author: Ming
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0
month = 0

previousBalance = balance
while month < 12:
    minimumMonthlyPayment = monthlyPaymentRate*previousBalance
    monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    previousBalance = updatedBalanceEachMonth 
    month += 1
print('Remaining Balance: ' + str(round(previousBalance, 2))) 