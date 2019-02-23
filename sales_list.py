# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:21:48 2019

@author: timov
"""

list_size = 5
i = 0
number_list = []

while i < list_size:
    i += 1
    str_i = str(i)
    number = input("Day #" + str_i + ": ")
    number = float(number)
    number_list += [number]
    
for item in number_list:
    print(item)
    
    
    
    
                 
