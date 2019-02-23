# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:12:55 2019

@author: timov
"""

name = input("What is your name? ")
age = input("What is your age? ")
income = input("What is your income? ")

print("Here is the data you entered:")
print("Name: " + name)
print("Age: " + age)
print("Income: " + format(float(income), ".1f"))