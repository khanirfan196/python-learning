
class Vehicle:
    def __init__(self, engine, transmission, tyres, chassy):
        self.engine = engine
        self.transmission = transmission 
        self.tyres = tyres
        self.chassy = chassy 

    def __str__(self):
        return f"The engine is of {self.engine}, transmission is of {self.transmission}, vehicle has {self.tyres} tyres and its chassy is of {self.chassy}"
    
    def vehicle_func(self):
        print("this is vehicle function")
        return self
        
    
class Cars(Vehicle):
    def __init__(self, engine, transmission, tyres, chassy, vehicle_type):
        super().__init__(engine, transmission, tyres, chassy) 
        # or Vehicle.__init__(engine, transmission, tyres, chassy)
        # But super() automatically inherits the parents __init__. 
        self.vehicle_type = vehicle_type

    # Overriding this function
    def vehicle_func(self):
        print(f"The vehicle is of type {self.vehicle_type}")
        return self 
    
    def vehicle_func_2(self):
        print(f"The vehicle is of type {self.vehicle_type}")
        return self 
    
    

    
car1 = Cars("v4", "axle", "4", "basic", "car")

print(car1)

# Below way is called method chaninig via 
car1.vehicle_func().vehicle_func_2()

        