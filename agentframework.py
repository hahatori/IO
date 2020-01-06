# Import the random module using the import statement.
import random 

# Build the Agent class.
class Agent(): 
    
    # Define the initialization method.
    def __init__(self, environment):  # The first argument of __init__ is always self, environment is formal parameter.
        self.environment = environment # Pass the environment list to the Agent's constructor.
        self.store = 0
        self.y = random.randint(0,99) # Generate a random number between 0 and 99 and assign it to y.
        self.x = random.randint(0,99) # Generate a random number between 0 and 99 and assign it to x.
    
    # Define the move method, use if...else statement and Torus to deal with boundary issues.
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
            
    # Define the eat method, use if statement to work out.
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
        self.store += 10 
    
    # This method returns a string repersenting that object when we use the print statement.   
    def __str__(self):
       return "y= %s, x= %s" % (self.y, self.x)


# Creat objects to test print.           
a = Agent("environment")

print(a.move, a.eat) #Locations.
print("Location:%s" % id(a), a)# Display the location and stores information.
#print(type(a)) 







