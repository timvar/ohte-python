# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:26:17 2019

@author: timov
"""

def main():
    text = input("Enter string: ")
    count = 0
    for c in text:
        if c == 'T':
            count = count + 1
        if c == 't':
            count = count + 1
    
    print(str(count))

main()      
   