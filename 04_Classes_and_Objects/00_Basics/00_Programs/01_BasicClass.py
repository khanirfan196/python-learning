
class DemoClass:
    def __init__(self, name, email):
        self.name = name
        self.email = email 

    def __str__(self):
        return f"The name is {self.name}, and email is {self.email}"
    
    def demofunc(self):
        return "Hello, this is from function"
    

obj1 = DemoClass("irfan", "irfan@gmail.com")


print(obj1)
print(obj1.demofunc())

# We can delete the object using 'del' keyword