import random 

# Build the class.
class Agent(): 
    
    # Define methods.
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
    
    # This method returns a string repersenting that object when we use the print statement.   
    def __str__(self):
       return "y= %s, x= %s" % (self.y, self.x)

# Creat objects to test print.           
a = Agent("environment")
print(a.move, a.eat) #Locations.
print("Location:%s" % id(a), a)# Display the location and stores information.
#print(type(a)) 







