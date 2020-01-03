#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:05:27 2019

@author: toriliang
"""
import random 
import matplotlib.pyplot

class Agent():
    def __init__(self, environment):
        self.environment = environment
        self.store = 0
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
    
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
        self.store += 10 
            
a = Agent("environment")
print(a.y, a.x)

a.move()
print(a.y, a.x)

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)