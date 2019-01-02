# -*- coding: utf-8 -*-
"""

@author: Koti Vellanki
"""

import sys

class Banking:
    bank = 'SBI'
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance = self.balance + amt
        print()
        print('Your Balance after deposit is :',self.balance)
    def withdraw(self,amt):
        try:
            if amt > self.balance:
                print()
                print('Insufficient Balance...,your balance is :',self.balance)
                sys.exit()
            self.balance = self.balance - amt
            print()
            print('Balance after withdraw is:',self.balance)
        except Exception:
            self.balance = self.balance - amt
            print()
            print('Balance after withdraw is:',self.balance)
    
name = input('Enter Your Name :')
print('{} Bank Welcomes you {}'.format(Banking.bank,name))

customer = Banking(name)

while True:
    print('Banking Features:\nD-Deposit\nW-Withdraw\nE-Exit')
    option = input('Enter Your Option:')
    if option in ['d','D']:
        amt = float(input('Enter Amount for Deposit:'))
        customer.deposit(amt)
    elif option in ['w','W']:
        amt = float(input('Enter Amount to Withdraw:'))
        customer.withdraw(amt)
    elif option in ['e','E']:
        print()
        print('Thanks for Banking with {}'.format(Banking.bank))
        sys.exit()
    else:
        print()
        print('Please Choose the valid option............')
