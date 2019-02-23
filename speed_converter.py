# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:13:54 2019

@author: timov
"""
print("KPH", "\t", "MPH")
print("----------------")
for speed in range(60, 140, 10):
    print(speed, "\t", format(speed/1.609344, ".1f"))
    