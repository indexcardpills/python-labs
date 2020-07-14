'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''

class Central_America:
    def __init__(self, region, city, country):
        self.region=region
        self.city=city
        self.country=country

    def __str__(self):
        return f"{self.city} is a city in {self.country} in {self.region}."


class Caribbean:
    def __init__(self, region, city, country):
        self.region=region
        self.city=city
        self.country=country

    def __str__(self):
        return f"{self.city} is a city in {self.country} in the {self.region}."

class South_America:
    def __init__(self, region, city, country):
        self.region=region
        self.city=city
        self.country=country

    def __add__ (self, other):
        '''other must be type South America'''
        #return self.country+other.region
        return self.country+" is a country in South America"

    def __str__(self):
        return f"{self.city} is a city in {self.country} in {self.region}."


#print(colombia.addition("hello"))
antigua=Central_America("Central America", "Antigua", "Guatemala")
sps=Central_America("Central America", "San Pedro Sula", "Honduras")
kingston=Caribbean("Caribbean", "Kingston", "Jamaica")
ponce=Caribbean("Caribbean", "Ponce", "Puerto Rico")
medellin=South_America("South America", "Medellin", "Colombia")
riobamba=South_America("South America", "Riobamba", "Ecuador")
print(antigua, sps, kingston, ponce, medellin, riobamba)
#mix=South_America(medellin+riobamba)
colombia=South_America("south america", "bogota", "colombia")
#print(colombia.__add__("hello"))
print(colombia+medellin)