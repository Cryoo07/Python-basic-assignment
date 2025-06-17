from animal import Animal

class Lion(Animal):
    def make_sound(self):
        return "Roarrr!"

    def feed(self):
        return f"{self._name} the lion is fed meat at {self._feeding_time}."

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

    def feed(self):
        return f"{self._name} the elephant is fed grass and fruits at {self._feeding_time}."

class Parrot(Animal):
    def make_sound(self):
        return "Squawk!"

    def feed(self):
        return f"{self._name} the parrot is fed seeds at {self._feeding_time}."
