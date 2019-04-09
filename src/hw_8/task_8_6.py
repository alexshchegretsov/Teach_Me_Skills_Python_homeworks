"""
Дан массив целых чисел A.
Найти суммы положительных и
отрицательных элементов массива,
используя функцию определения суммы.
"""
from random import randint as rd
from typing import Union


def sum_of_positive_and_negative(*args) -> Union[int, tuple]:
    """Returns the sum of positive and sum of negative elements"""

    all_summ = sum(args)
    for x in args:
        if x > 0:
            all_summ -= x
    negative = all_summ
    positive = sum(args) - negative
    return positive, negative


A = [rd(-30, 30) for _ in range(10)]
pos, neg = sum_of_positive_and_negative(*A)
print(pos, neg)
