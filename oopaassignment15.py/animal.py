from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._feeding_time = None

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self):
        pass

    def set_feeding_time(self, time):
        self._feeding_time = time

    def get_feeding_time(self):
        return self._feeding_time

    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}, Next Feeding: {self._feeding_time}"
