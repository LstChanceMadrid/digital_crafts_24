#class is a blueprint always singular

#blueprint (properties)    property - atribute
#(ex. Table)
#-surface
#-material
#-4 legs
#- cost

#actions --
#- start()
#- stop()

#object uses a Class blueprint

class Car:

    #initializer or a constructor
    def __init__(self, make, model, year):
         #self is the instance\object of the Car class
        self.make = make
        self.model = model
        self.year = year
        self.is_state_inspection_passed = False
        print("initializing a car")
        print(self)
    def start(self):
        print("starting the car")
    def perform_inspection(self):
        print("Performing state inspection...")
        self.is_state_inspection_passed = True
    def describe_car(self):
        print("Make - " + self.model)


#creating an instance/object of Car class
car = Car('Honda', 'Accord', '2011')


print(car.make)
print(car.model)
print(car.year)
print(car.is_state_inspection_passed)
car.start()


car.perform_inspection()
print(car.is_state_inspection_passed)

car.describe_car()


#toyota = Car():

#class DrivingLicense:
#    def __init__(self, first_name, last_name, date)

honda = {"make": "Honda", "model": "Accord"}




class Address:
    def __init__(self):
        self.street = "1200 Richmond Ave"
        self.state = "TX"
        self.city = "Houston"


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.addresses = []




user = User("John", "Doe", 29)

address1 = Address()
address2 = Address()
#sets the address of the user
user.addresses.append(address1)
user.addresses.append(address2)

print(len(user.addresses))