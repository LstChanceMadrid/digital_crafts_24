
#Basics


class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.num_of_greetings = 0

    def __repr__(self):
        return "Person {0} {1} {2}".format(self.name, self.email, self.phone)

    def greet(self, other_person):
        print('Hello {0}, I am {1}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print("{0}'s email: {1}, {0}'s phone number: {2}".format(self.name, self.email, self.phone))

    def add_friend(self, other_person):
        self.add_friend = self.friends.append(other_person.name)

    def num_friends(self):
        print(len(self.friends))

    def greeting_count(self):
        print(self.num_of_greetings)
        self.num_of_greetings += 1






sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")


sonny.greeting_count()

sonny.greet(jordan)
jordan.greet(sonny)

sonny.greeting_count()

print(sonny.email + " " + sonny.phone)
print(jordan.email + " " + jordan.phone)

sonny.print_contact_info()

sonny.add_friend(jordan)
print(sonny.friends)

sonny.num_friends()

print(sonny)



class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print("{0} {1} {2}".format(self.year, self.make, self.model))


car = Vehicle('Nissan', 'Leaf', 2015)
print(car.make)
print(car.model)
print(car.year)
car.print_info()



