'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Central_America:
    def __init__(self, region, city, country):
        self.region=region
        self.city=city
        self.country=country

    def __str__(self):
        return f"{self.city} is a city in {self.country} in {self.region}."


class Guatemala(Central_America):
    def __init__(self, language, population):
        self.language=language
        self.population=population

    def __str__(self):
        return f"The population of {self.country} is {self.population} and they speak {self.language}"

class Antigua(Central_America):
    def __init__(self, city, population, language):
        self.city=city
        self.population=population
        self.language=language

    def __str__(self):
        return f"The population of {self.city} is {self.population} and they speak {self.language}"


class Caribbean:
    def __init__(self, region, city, country):
        self.region=region
        self.city=city
        self.country=country

    def __str__(self):
        return f"{self.city} is a city in {self.country} in the {self.region}."


class Cuba(Caribbean):
    def __init__(self, language, population):
        self.language=language
        self.population=population

    def __str__(self):
        return f"The population of {self.country} is {self.population} and they speak {self.language}"


class Havana(Caribbean):
    def __init__(self, city, population, language):
        self.city = city
        self.population = population
        self.language = language


class HistoricCenter(Havana):
    def __init(self, neighborhood):
        self.neighborhood=neighborhood


class South_America:
    def __init__(self, region, city, country):
        self.region=region
        self.city=city
        self.country=country


    def __str__(self):
        return f"{self.city} is a city in {self.country} in {self.region}."


