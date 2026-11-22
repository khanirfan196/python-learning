
class ToyotaCar:
    
    car = "Toyota Corolla"

    def buildcar():
        print("Toyota Corolla 2025 is build.")



if __name__ == "__main__":

    print(ToyotaCar.car)
    ToyotaCar.buildcar()

    toy = ToyotaCar()

    print("Accessing class method through instance.")
    toy.buildcar()

