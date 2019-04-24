from random import randint as rd


class Pet:
    __counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True
        Pet.__counter += 1

    @classmethod
    def get_counter(cls) -> int:
        """Return class private attribute"""
        return cls.__counter

    @classmethod
    def get_random_name(cls) -> str:
        """Return random name in format [A-Z]-[0-100]"""
        return f'{chr(rd(65,90))}-{rd(0,100)}'

    def change_weight(self, value=None):
        self.weight += 0.2 if not value else value

    def change_height(self, value=None):
        self.height += 0.2 if not value else value

    def jump(self):
        print('SH sh s hs h  jump')

    def run(self):
        print('shhhhhh')

    def birthday(self):
        self.age += 1

    def voice(self):
        pass


class Dog(Pet):

    def birthday(self):
        if self.is_alive:
            super().birthday()
            self.is_alive = True if self.age < 13 else False

    def voice(self):
        print('Wooof')


class Cat(Pet):

    def voice(self):
        print('Meooooww!')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            self.is_alive = True if self.age < 16 else False


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def fly(self):
        if self.weight > 0.1:
            print('This parrot cannot fly')
        else:
            print('Wings!! Fly away!')

    def change_weight(self, value=None):
        self.weight += 0.05 if not value else value

    def change_height(self, value=None):
        self.height += 0.05 if not value else value

    def birthday(self):
        if self.is_alive:
            super().birthday()
            self.is_alive = True if self.age < 60 else False

    def voice(self):
        print('Kaaaaarrrr')


class Horse(Pet):
    def voice(self):
        print('Igogog')


class Donkey(Pet):
    def voice(self):
        print('Ishshssaaaa')


class Mule(Donkey, Horse):
    pass
