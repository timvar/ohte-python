# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 07:49:22 2019

@author: timov
"""

def get_login_name():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    s_id = input("Enter your studen ID number: ")
             
    login_name = first[0:3] + last[0:3] + s_id[-3:]

    print(login_name)
    