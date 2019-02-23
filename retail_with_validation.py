# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:04:44 2019

@author: timov
"""

cost = input("Enter the item's wholesale cost: ")
cost = float(cost)

while cost <= 0:
    print("ERROR: the cost cannot be negative.")
    cost = input("Enter the correct wholesale cost: ")
    cost = float(cost)
    
print("Retail price: ", cost * 2.5)


    