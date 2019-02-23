# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:18:55 2019

@author: timov
"""

sales_file = open('sales.txt', 'w')
days = input("For how many days do you have sales? ")
days = int(days) + 1

for count in range(1, days):
    count = str(count)
    sales = input("Enter the sales for day #" + count + ": ")
    sales_file.write("Day #" + count + ": " + sales + "\n")
    
    
sales_file.close()