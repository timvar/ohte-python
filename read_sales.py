# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 19:34:41 2019

@author: timov
"""

file_name = input("Enter filename: ")

input_file = open(file_name, 'r')
line = input_file.readline()

while line != "":
    number = float(line)
    print(format(number, ".2f"))
    line = input_file.readline()
    
input_file.close()