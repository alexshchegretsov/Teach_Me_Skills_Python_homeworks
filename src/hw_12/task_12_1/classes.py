class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True

    def run(self):
        print('Ruuun')

    def jump(self):
        print('Shhhhhh jump')

    def birthday(self):
        self.age += 1

    def change_weight(self, value=None):
        self.weight += .2 if not value else value

    def change_height(self, value=None):
        self.height += .2 if not value else value

    def voice(self): pass


class Dog(Pet):

    def voice(self):
        print('Wwwoooof!')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            self.is_alive = False if self.age > 13 else True


class Cat(Pet):

    def voice(self):
        print('Meowww')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            self.is_alive = False if self.age > 16 else True


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def fly(self):
        if self.weight > .1:
            print(f'This parrot cannot fly coz weight = {self.weight}')
        else:
            print('Flyyyyyyyy')

    def change_weight(self, value=None):
        self.weight += .05 if not value else value

    def change_height(self, value=None):
        self.height += .05 if not value else value

    def birthday(self):
        if self.is_alive:
            super().birthday()
            self.is_alive = False if self.age > 60 else True
