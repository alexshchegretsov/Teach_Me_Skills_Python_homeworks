class Dog:
    def __init__(self, name, height, weight, age, master, address='Minsk'):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__master = master
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


# dog = Dog()  # создём объект(экземпляр) класс
dog_1 = Dog('Bob', 30, 50, 5, 'alex')
dog_2 = Dog('Box', 20, 40, 15, 'john')
print(dog_1.name)