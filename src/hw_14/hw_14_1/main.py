from classes_hw_14 import (
    Dog,
    Wolf,
    Cat,
    Lion,
)


def main():
    dog_1 = Dog('Altay', 20, .5, 15, 4, 'grey', 'red')
    wolf_1 = Wolf('Volk', 30, .5, 10, 4, 'green', 'grey')
    cat_1 = Cat('Zhook', 7, .2, 8, 4, 'green', 'black')
    lion_1 = Lion('leo', 35, .6, 16, 4, 'blue', 'sand')
    dog_1.sled()
    dog_1.swim()
    dog_1.voice()
    wolf_1.sled()
    wolf_1.swim()
    wolf_1.voice()
    cat_1.scratchy()
    cat_1.climb_on_tree()
    cat_1.voice()
    lion_1.scratchy()
    lion_1.climb_on_tree()
    lion_1.voice()


if __name__ == '__main__':
    main()
