
class Battery:
    def __init__(self, life, manufacturer):
        self.life = life
        self.manufacturer = manufacturer

    def __repr__(self):
        return "Battery Information"




class ElectricCar:
    def __init__(self, make, model, battery):
        self.make = make
        self.model = model
        self.battery = battery

    def pretty_print(self):
        print("make = {0}, Model = {1}".format(self.make, self.model))
        print(self.battery)


        #self.battery_life = 100
        #self.battery_manufacturer = "CC"
#create ojbect of battery class
battery = Battery(100, "CC")

#object car and pass object battery
car = ElectricCar("Tesla", "Model", "X")

car.pretty_print()

