class Car:
    def __init__(self, model, year, speed):
        self.name = model
        self.year=year
        self.speed=speed

    def accelerate(self):
       self.speed += 5
       return self.speed

    def brake(self):
        if self.speed>0:
           self.speed -= 5
           return self.speed
        else:
            print("the speed is already 0")

    def honk_horn(self):
       print(f"{self.name} goes beep beep")


x = Car("Nissan", 1999, 60)
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
x.brake()
print(x.speed)
x.honk_horn()