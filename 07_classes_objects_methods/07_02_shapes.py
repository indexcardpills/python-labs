'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math
class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def rect_area(self):
        return self.length*self.width

    def rect_perimeter(self):
        return self.length*2+self.width*2


class Circle:
    def __init__(self, radius):
        self.radius=radius

    def circle_area(self):
        return math.pi*self.radius**2

    def circle_circum(self):
        return 2*math.pi*self.radius

x=Rectangle(5, 10)
print(x.rect_area())
print(x.rect_perimeter())
y=Circle(4)
print(y.circle_area())
print(y.circle_circum())


