class Enclosure:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(animal.get_details())

    def feed_all(self):
        for animal in self.animals:
            print(animal.feed())

    def make_all_sounds(self):
        for animal in self.animals:
            print(f"{animal._name} says {animal.make_sound()}")
