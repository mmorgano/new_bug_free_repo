print("Ciao mondo")
# create a new class to model a car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    def __repr__(self): 
        return f"{self.year} {self.make} {self.model}"
# create a new instance of the class Car

car = Car("Renault", "Clio", 2019)
print(car)
