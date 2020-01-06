# I/O

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

### 

It generates a random number of characters from 0 to 1 (0 <= n < 1.0):

```sh
$ random.random()
```

It generates a random number n (12 <= n <= 20):

```sh
$ random.randint(12, 20)
```

Error:

```sh
$ random.randint(20, 12)
```

## Theoretical Results

Expect to move random coordinate points and calculate the distance between two sets of them, then show the 10 points in a scatter plot with x and y axes of 0 to 99. 

## Actual Results

![Scatter Plot](https://github.com/hahatori/Python_Assignment1/blob/master/AgentPlot.png)

## Issues

1. Agents can only eat 10 units at a time. If there are less than 10 left, can they eat the last few without leaving a negative value?

2. The question of by finding the size of the agent's internal environment and using the size when randomly assigning their starting positions and working with boundary conditions, the agent can wander through the environment.

3. If the agent has greedy guts and eats more than 100 units, can you get the agents to sick up their store in a location?



