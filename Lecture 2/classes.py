# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:30:32 2021

@author: Admin
"""
class Flights():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flights(3)

people = ["Thien","Vinh","Long","Truong"]
for person in people:    
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successed.")
    else:
        print(f"No available seat for {person}.")