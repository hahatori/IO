Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
class Rocket():

    current_coordinates = [0,0]
    launched = False
    start = [0,0]
    
    def set_start_location(self,coordinates):
        self.start = coordinates
        self.current_coordinates[0] = coordinates[0]
        self.current_coordinates[1] = coordinates[1]
        # now try uncommenting the following:
        # self.current_coordinates = [coordinates[0],coordinates[1]]
        # Why do you think there's a difference?
        
    def update_location(self):
        if self.launched:
            self.current_coordinates[0] = self.current_coordinates[0] + 1
            self.current_coordinates[1] = self.current_coordinates[1] + 1
        else:
            self.current_coordinates[0] = self.start[0]
            self.current_coordinates[1] = self.start[1]
            

>>> object.__str__()

def __str__(self) :
	return "Hi I'm an agent"
