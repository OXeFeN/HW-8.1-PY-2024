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
    
    def new_car():
        model = input("Insert model: ")
        release = input("Insert year of release: ")
        manufacturer = input("Insert manufacturer: ")
        engine = input("Insert engine capacity (in liters): ")
        color = input("Insert color: ")
        price = input("Insert price: ")

        return Car(model=model, years_of_release=release, manufacturer=manufacturer, engine_capacity=engine, color=color, price=price)