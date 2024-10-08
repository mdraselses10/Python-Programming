# Base class representing an Animal
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball."

dog = Dog("Buddy", "Golden Retriever")

print(dog.make_sound())
print(dog.fetch())
