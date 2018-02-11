#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:53:51 2018

@author: jasonfaas
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def calculateRemainingBalance(balance, months):
    balanceAfterPayment = balance - balance * monthlyPaymentRate
    balanceAfterInterest = balanceAfterPayment + balanceAfterPayment * annualInterestRate/12
    newBalance = round(balanceAfterInterest, 4)
#    print("Month " + str(months) + " remaining balance:" + str(newBalance) + ":")
    if months == 12:
        return newBalance
    return calculateRemainingBalance(newBalance, months + 1)


print("Remaining balance: " + str(round(calculateRemainingBalance(balance, 1), 2)))