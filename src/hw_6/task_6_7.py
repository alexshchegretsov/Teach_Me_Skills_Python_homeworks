"""
Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали.

"""
from random import randint as rd

matrix = [[rd(-10, 20) for y in range(5)] for x in range(5)]

for i, row in enumerate(matrix):
    id_max = row.index(max(row))
    max_number = row[id_max]
    diagonal_number = row[i]
    max_number, diagonal_number = diagonal_number, max_number

print(matrix)
