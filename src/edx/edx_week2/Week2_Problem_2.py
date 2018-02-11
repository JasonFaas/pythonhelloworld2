#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:12:41 2018

@author: jasonfaas
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:53:51 2018

@author: jasonfaas
"""

balance = 3926
annualInterestRate = 0.2

def calculateRemainingBalance(balance, months, monthlyPayment):
    balanceAfterPayment = balance - monthlyPayment
    balanceAfterInterest = balanceAfterPayment + balanceAfterPayment * annualInterestRate/12
    newBalance = round(balanceAfterInterest, 4)
#    print("Month " + str(months) + " remaining balance:" + str(newBalance) + ":")
    if months == 12:
        return newBalance
    return calculateRemainingBalance(newBalance, months + 1, monthlyPayment)

currentResult = round(calculateRemainingBalance(balance, 1, balance), 2)
if currentResult > 0:
    print("WHAT?!?")
else:
    high = balance
    low = 0
    current = balance/2
    currentResult = round(calculateRemainingBalance(balance, 1, current), 4)
    while currentResult != 0 and current > 0:
#        print("Attempt result:" + str(round(currentResult, 4)) + ":" + str(round(current, 4)))
        if currentResult > 0:
            low = current
            current = high - ((high - low) / 2)
        else:
            high = current
            current = high - ((high - low) / 2)
        currentResult = round(calculateRemainingBalance(balance, 1, current), 1)

print("Lowest Payment: " + str(round((current+5)/10)*10))
