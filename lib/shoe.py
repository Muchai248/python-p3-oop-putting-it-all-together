#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = "New"
    def get_size(self):
        return self._size

    def set_shoe_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self._size = size
    def cobble(self):
        print("Your shoe is as good as new!")

    size = property(get_size, set_shoe_size)
ndula=Shoe("Nike", 4)
ndula.size = '8'
print(ndula.size)
print(ndula.cobble())