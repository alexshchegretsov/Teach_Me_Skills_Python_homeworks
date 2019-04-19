class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True

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


class Dog(Pet):

    def bark(self):
        print('WWooooooff!')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            self.is_alive = True if self.age < 13 else False


class Cat(Pet):

    def meow(self):
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
