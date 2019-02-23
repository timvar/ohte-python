# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 20:33:06 2019

@author: timov
"""
import os
temp_file = open('temp.txt', 'w')
coffee_file = open("coffee.txt", 'r')
coffee_to_remove = input("Enter coffee to be removed: ")
coffee_to_remove = coffee_to_remove.rstrip("\n")
line = coffee_file.readline()
line = line.rstrip("\n")

while line != "":
    if coffee_to_remove != line:
        temp_file.write(line + "\n")
    line = coffee_file.readline()
    line = line.rstrip("\n")
  
coffee_file.close()
temp_file.close()
os.remove("coffee.txt")
os.rename("temp.txt", "coffee.txt")

