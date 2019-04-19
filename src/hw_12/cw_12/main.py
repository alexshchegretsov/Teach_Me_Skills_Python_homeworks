from cw_12 import (
    Dog,
    Cat,
    Parrot,
)


def main():
    dog_1 = Dog('Druzhok', 5, 'Alex', 20, 0.5)
    cat_1 = Cat('Zhook', 18, 'john', 10, 0.2)
    parrot_1 = Parrot('Alexei', 80, 'Oleg', 10, 0.1,'Ara')
    dog_1.bark()
    cat_1.meow()
    parrot_1.fly()
    # parrot_1.birthday()
    # parrot_1.change_weight()
    # cat_1.birthday()
    # print(cat_1.age)
    # print(cat_1.is_alive)
    print(parrot_1.species)


if __name__ == '__main__':
    main()
