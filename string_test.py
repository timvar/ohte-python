# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 08:30:47 2019

@author: timov
"""

def main():
    text = input("Enter a string: ")
    print("This is what I found about that string:")

    if text.isalnum():
        print("The string is alphanumeric.")

    if text.isalpha():
        print("The string contains only alphabetic characters.")

    if text.islower():
        print("The letters in the string are all lowercase.")
        
    if text.isupper():
        print("The letters in the string are all uppercase.")
        
    if text.isdigit():
        print("The string contains only digits.")
        
main()
        
    
    
