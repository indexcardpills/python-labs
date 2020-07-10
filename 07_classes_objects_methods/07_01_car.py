'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    def __init__(self, model, year, max_speed):
        self.name = model
        self.year=year
        self.speed=max_speed

    def accelerate(self):
       self.speed += 5
       return self.speed

    def __str__ (self):
        return f"The car is a {self.year} {self.name} with a max speed of {self.speed} mph"

x=Car("Honda", 2016, 140)
print(x)
y=Car("Lexus", 2020, 180)
print(y)
x.accelerate()
y.accelerate()
print(x,y)
