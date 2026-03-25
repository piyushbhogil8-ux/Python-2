# Base class
class vehicle:
    def move(self):
        print("the vehical is moving")


# Subclass car
class car(vehicle):
    def move(self):
        print("Driving on Road")

# Subclass bicycle 
class bicycle(vehicle):
    def move(self):
        print("Padeling on the road")

# Deconstrating Polymorphism
vehicle = [car(),bicycle()]

for v in vehicle:
    v.move()
