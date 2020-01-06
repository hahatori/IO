# I/O
(Input/Output)
This project including [in.txt](https://github.com/hahatori/IO/blob/master/in.txt), [agentframework.py](https://github.com/hahatori/IO/blob/master/agentframework.py) and [model.py](https://github.com/hahatori/IO/blob/master/model.py).

## Contents

- [Details](#details)
- [Theoretical Results](#theoretical_result)
- [Actual Results](#actual_result)
- [Issues](#issues)

## Details

### The key elements:

**in.txt** is a text file with raster data.

**Agent** code can build agents to interact.

**Model** code can creat models for connecting developers and users.

### OOP (Object Oriented Programming)

**Creat Class, Object and Method**

```sh
$ class Agent:   # Creat "Agent" class.    
      def eat(self): # Define "eat" method.
      pass    #An empty block.
      
  a = Agent() #Creat a object.
  a.eat()
  print a
```

**agentframework.py** :

```sh
$ import random 

  class Agent(): 

      # # Define the initialization method.
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

      def __str__(self):
         return "y= %s, x= %s" % (self.y, self.x)
          
  a = Agent("environment")
  
  print(a.move, a.eat) #Locations.
  print("Location:%s" % id(a), a)
```

Output:

```sh
$ <bound method Agent.move of <__main__.Agent object at 0x117326a10>> <bound method Agent.eat of <__main__.Agent object at 0x117326a10>>
  Location:4684147216 y= 15, x= 36
```

Error:

```sh
$ random.randint(20, 12)
```
### 

## Theoretical Results

Expect to move random coordinate points and calculate the distance between two sets of them, then show the 10 points in a scatter plot with x and y axes of 0 to 99. 

## Actual Results

![Scatter Dots Plot](https://github.com/hahatori/Python_Assignment1/blob/master/IO.png)

## Issues

1. Agents can only eat 10 units at a time. If there are less than 10 left, can they eat the last few without leaving a negative value?

2. The question of by finding the size of the agent's internal environment and using the size when randomly assigning their starting positions and working with boundary conditions, the agent can wander through the environment.

3. If the agent has greedy guts and eats more than 100 units, can you get the agents to sick up their store in a location?



