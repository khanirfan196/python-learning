

class Vehicle:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def engine_start(self):
        return "Vehicle engine started"

    def class_method():
        return "This is a class method"


if __name__ == "__main__":
    car = Vehicle("Toyota", "Camry", 2026)

    print(car.engine_start())

    print("Trying to access instance method from Vehicle Class")

    print(Vehicle.class_method())
    # Above will print the return statement of the method.
    print(Vehicle.engine_start())
    # Above print statement will end up in error.