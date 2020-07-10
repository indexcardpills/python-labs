'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:
    #to build this thing
    def __init__(self, name_to_pass, system):
        self.name=name_to_pass
        self.system=system

    def print_solar_system(self):
        print(self.system)

    def __str__(self):
        return f"The name of the planet is {self.name} and the system is {self.system}"


earth=Planet("Earth", "solar")
print(earth.name)
print(earth.system)
print(earth)

