# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:08:32 2021

@author: Admin
"""
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    #sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Can't divide by 0")
    #sys.exit(1)
        
print(f"{x} / {y} = {result}")