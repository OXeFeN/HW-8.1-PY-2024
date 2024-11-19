#Task 1
#Implement a class Car. Class fields should store the following: model, year of release, manufacturer, engine capacity, color, price. 
#Implement class methods for data input and output, provide access to individual fields through class methods


class Car:
    def __init__(self, model, years_of_release, manufacturer, engine_capacity, color, price):
        self.model = model
        self.release = years_of_release
        self.manufacturer = manufacturer
        self.engine = engine_capacity
        self.color = color
        self.price = price

    def __str__(self):
        return (f"{self.manufacturer} {self.model} ({self.release}):\n Barva: {self.color}\n Motor: {self.engine} L\n Cena: {self.price} Kč")