

from abc import ABC, abstractmethod  # import abstract based class

# custom exeption


class InvalidOperationError(Exception):
    pass


class Stream(ABC):  # inherite from ABC then cannot be intantiated
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream us already closed")
        self.opened = False

    @abstractmethod  # now all classes inheriting teh STream class have to impl the read methd
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data fron a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data fron a Network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


stream = MemoryStream()


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2
        print("Mamal Constructor")

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swin")


# m = Mammal()
# print(m.age)
# print(m.weight)
