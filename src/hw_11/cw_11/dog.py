class Dog:
    def __init__(self, name, color, master):
        self.name = name
        self.color = color
        self.__master = master

    def bark(self):
        print('Wooof!')

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self,master):
        self.__master = master


dog_1 = Dog('Bob', 'black', 'Alex')
dog_1.master = 'oleg'
print(dog_1.master)

