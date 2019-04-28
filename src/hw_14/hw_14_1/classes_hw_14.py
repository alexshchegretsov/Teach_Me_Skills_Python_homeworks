# классы остаются абстрактными если они не переопределили abstractmethod
# интерфейсы не описывают состояния
# abstractclass - безэкземплярный класс, класс экземпляр которого нельзя создать
# разделять по файлам - интерфейсы, миксины, классы.
# константы - MY_CONST
"""

Создать иерархию(слайды 49-50).
Добавить конструктор в родительский класс Animal.
Добавить абстрактный метод voice в класс Animal.
Переопределить метод voice в классах Dog, Wold, Lion, Cat.
Добавить два абстрактных метода в интерфейсы.
Переопределить их в дочерних классах.
Создать объекты классов Dog, Wold, Lion, Cat.
Вызвать каждый из метод каждого объекта.

"""

from abc import ABC, abstractmethod
from interfaces import CanineInterface, FelineInterface


class Animal(ABC):
    def __init__(self, name, weight, height, age, legs, eye_color, futher_color):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.legs = legs
        self.eye_color = eye_color
        self.futher_color = futher_color

    @abstractmethod
    def voice(self):
        pass


class Pet(Animal):
    pass


class Cat(Pet, FelineInterface):
    pass

    def voice(self):
        print('Meeoow')

    def scratchy(self):
        print('Cat scratchy')

    def climb_on_tree(self):
        print('Cat climbing anywhere')


class Dog(Pet, CanineInterface):
    pass

    def voice(self):
        print('Wooooof')

    def swim(self):
        print('Dog swim thru the river')

    def sled(self):
        print('Dog take sled')


class WildAnimal(Animal):
    pass


class Wolf(WildAnimal, CanineInterface):
    pass

    def voice(self):
        print('WOoooolf')

    def swim(self):
        print('Wolf swimming thru the river')

    def sled(self):
        print('Wolf take sled')


class Lion(WildAnimal, FelineInterface):
    pass

    def voice(self):
        print('Lion AAAaaaaaaau')

    def scratchy(self):
        print('Lion scratchy')

    def climb_on_tree(self):
        print('Lion climb on tree')
