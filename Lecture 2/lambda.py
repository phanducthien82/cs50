# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:02:52 2021

@author: Admin
"""

names = [
        {"name":"Thien","house":"Nam Dinh"},
        {"name":"Hue","house":"Ninh Binh"},
        {"name":"Truong","house":"Thai Binh"}
    ]

names.sort(key = lambda person: person["name"])

print(names)