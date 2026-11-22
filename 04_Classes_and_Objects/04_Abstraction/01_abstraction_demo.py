from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def engine(self):
        pass 


class Car(Vehicle):
    def __init__(self, body, make, model, year):
        self.body = body
        self.make = make 
        self.model = model 
        self.year = year
        self.pistons = None 
        self.fuel = None

        
    def engine(self):
        if self.body in ["sedan", "hatchback"]:
            self.pistons = 4 
            self.fuel = "gasoline"
        return f"Its engine has {self.pistons} pistons and {self.fuel} type fuel."

    def __str__(self):
        return f"""
        Car body is {self.body} type, made by {self.make}, 
        model is {self.model} and of year {self.year}.
        {self.engine()}"""


if __name__ == "__main__":
    car_01 = Car("sedan", "toyota", "camry", 2026)

    print(car_01)