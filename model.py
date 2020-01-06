import random
import operator
import matplotlib.pyplot as plt  # Import package and change its name to plt.
import agentframework
import csv      # Import the csv module.

# Define a function and calculate the distance between two points.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Define arguments.
num_of_agents = 10      # Make a num_of_agents variable and assign it the value 10
num_of_iterations = 100 # Make a num_of_iterations variable and assign it the value 100
agents = []             # Creat agents list.
environment = []        # Creat environment list.

# Read the in.txt into the environment list.
#f=open("in.txt",delimiter=',')
#data = csv.reader(f)
with open("in.txt") as f:
    data = f.read().splitlines() 

    for row in data:
        rowlist = []
        for value in row.split(','): # Change data from in.txt into standard data. 
            if value[-1] == '\\':
                value1 = value[0:(len(value)-1)]
                rowlist.append(int(value1))
            else:
                rowlist.append(int(value))
        environment.append(rowlist) # Read the csv into the environment list.
        
for line in agents:
    f.write(line)
#f.close()


# Make the agents by putting into a for-loop.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
    plt.scatter(agents[i].x,agents[i].y)


# Move the agents by putting into nest for-loops.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()  # Calling move method from agent.
        agents[i].eat()   # Calling eat method from agent.

        
# Show the data plot.
plt.xlim(0, 100)          # Set the x-axis range from 0 to 100.
plt.ylim(0, 100)          # Set the y-axis range from 0 to 100.
plt.title("Scatter Plot") # Set plot title.
plt.imshow(environment)   # Display an image on the axes.

# Use for-each loop iterator to put out agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
         
# Display the scatter dots plot.
plt.show()

        
        
        
 
