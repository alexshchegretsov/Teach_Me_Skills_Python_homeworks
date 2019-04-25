"""
Создать статичный метод get_random_name. Метод возвращает случайную строку вида A-42.

"""

from classes_13_1 import (
    Dog,
    Cat,
    Parrot,
    Pet,
    Mule,
    Horse,
    Donkey,
)


def main():
    dog_1 = Dog('Druzhok', 5, 'Alex', 20, 0.5)
    cat_1 = Cat('Zhook', 18, 'john', 10, 0.2)
    parrot_1 = Parrot('Alexei', 80, 'Oleg', 10, 0.1, 'Ara')
    print(Pet.get_counter())
    print(dog_1.get_counter())
    mule_1 = Mule('Ia', 20, 'Iakov', 40, 0.7)
    mule_1.voice()
    print(mule_1.get_random_name())

if __name__ == '__main__':
    main()
