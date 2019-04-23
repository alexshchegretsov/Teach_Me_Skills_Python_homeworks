from classes import (
    Dog,
    Cat,
    Parrot,
)


def call_voice(*args):
    [_.voice() for _ in args]


def main():
    dog_1 = Dog('Druzhok', 10, 'John', 15, 0.4)
    cat_1 = Cat('Zhook', 7, 'Alex', 8, 0.2)
    parrot_1 = Parrot('Alexey', 59, 'Oleg', 0.4, 0.2, 'ara')
    dog_1.change_weight(3)
    dog_1.change_height(.1)
    call_voice(dog_1, cat_1)


if __name__ == '__main__':
    main()
