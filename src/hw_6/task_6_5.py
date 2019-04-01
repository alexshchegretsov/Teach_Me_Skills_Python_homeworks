"""
В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить им все четные по значению элементы.

"""
from random import randint as rd

sequence = [rd(-10, 30) for i in range(19)]
max_number = max(sequence)
for i, number in enumerate(sequence):
    if not number % 2:
        sequence[i] = max_number

print(sequence)
