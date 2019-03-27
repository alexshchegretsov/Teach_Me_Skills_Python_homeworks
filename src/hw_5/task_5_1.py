"""
Дана целочисленная матрица размера 5х5. Получить новую матрицу
путем деления всех элементов данной матрицы на ее наибольший по
модулю элемент.

"""
from random import randint as rd

matrix = [[rd(-100, 100) for x in range(5)] for y in range(5)]

max_num = 0
for x in range(5):
    for y in range(5):
        if max_num < abs(matrix[x][y]):
            max_num = abs(matrix[x][y])

for x in range(5):
    for y in range(5):
        matrix[x][y] //= max_num                # whatever

print(matrix)
