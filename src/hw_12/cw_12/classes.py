class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Ruuun')

    def jump(self):
        print('Shhhhhh jump')

    def birthday(self):
        self.age += 1


class Dog(Pet):

    def bark(self):
        print('Wwwoooof!')


class Cat(Pet):

    def meow(self):
        print('Meowww')


class Parrot(Pet):

    def fly(self):
        print('Flyyyyyyyy')
