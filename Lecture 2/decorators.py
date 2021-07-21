# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:53:11 2021

@author: Admin
"""

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")
    
hello()