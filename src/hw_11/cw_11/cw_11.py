"""
OOP
"""


class Dog:
    def __init__(self, name, height, weight, age, master, address='Minsk'):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.__master = master
        self.__address = address

    def bark(self):
        print('Woof woooof!')

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def change_name(self, name):
        self.name = name

    def get_master(self):
        return self.__master

    def set_address(self, address):
        """Setter"""
        self.__address = address

    def get_address(self):
        """Getter"""
        return self.__address


# dog = Dog()  # создём объект(экземпляр) класс
dog_1 = Dog('Bob', 30, 50, 5, 'alex')
dog_2 = Dog('Box', 20, 40, 15, 'john')

# dog_1.change_name('Zhook')  # изменяли атрибут
# dog_2.change_name('Strelka')
# print(dog_1.name)
# поведение - описывется с помощью методов
# dog_1.bark()
# dog_1.run()
# обращение к атрибутам
# print(dog_1.name)
# print(dog_1.height)
# print(dog_1.weight)
# print(dog_1.age)
# print(dog_2.name)
# print(dog_2.height)
# print(dog_2.weight)
# print(dog_2.age)


# модификаторы доступа
# dog_1.get_master('Alex')
# геттеры и сеттеры
print(dog_1.get_address())
dog_1.set_address('Vilnius')
print(dog_1.get_address())
