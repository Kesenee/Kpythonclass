class Pets:
    dog = []
    def __init__(self, dogs):
        self.dogs = dogs
class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def description(self):
        return self.name, self.age
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)
    def eat(self):
        self.eat(self)
        self.is_hungry = False
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletvher", 7),
    Dog("Larry", 9)
]
my_pets = Pets(my_dogs)

print("I have {} degs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))
print("And they're all {}s, of course.".format(dog.species))




