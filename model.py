#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:24:10 2019

@author: tori
"""

import random
import operator
import matplotlib.pyplot as plt
import agentframework
import csv

# Calculate the distance between two points.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Define arguments.
num_of_agents = 10
num_of_iterations = 100
agents = []
#rowlist = []
environment = []
#distance = [] 

# Read the csv into the environment list.
#f=open("in.txt",delimiter=',')
#data = csv.reader(f)
with open("in.txt") as f:
    data = f.read().splitlines() 

    for row in data:
        rowlist = []
        for value in row.split(','):
            if value[-1] == '\\':
                value1 = value[0:(len(value)-1)]
                rowlist.append(int(value1))
            else:
                rowlist.append(int(value))
        environment.append(rowlist)
        
for line in agents:
    f.write(line)
#f.close()


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
    plt.scatter(agents[i].x,agents[i].y)


# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

        
# Show the data plot.
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("Scatter Plot")
plt.imshow(environment)

# Pull out agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
         

plt.show()

        
        
        
 
