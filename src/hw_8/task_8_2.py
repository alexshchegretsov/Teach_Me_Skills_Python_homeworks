"""
Дан список чисел. Посчитать сколько раз встречается каждое число.
Подсказка: для хранения данных использовать словарь.
Для проверки нахождения элемента в словаре использовать метод get()

"""


def counter(*args, **kwargs) -> dict:
    """
    The function checks how many times a specific number
    is repeated from the list and returns a pair of key - the number
    of repetitions  which recorded in the dictionary
    """
    for num in args:

        if not kwargs.get(num):
            kwargs[num] = 1
        else:
            kwargs[num] += 1

    return kwargs


dictionary = {}
numbers = [2, 7, 2, 6, 5, 8, 9, 44, 5, 44, 2, 5]
print(counter(*numbers, **dictionary))
