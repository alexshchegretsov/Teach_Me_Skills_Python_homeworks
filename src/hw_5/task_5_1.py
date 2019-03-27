"""
Дана целочисленная матрица размера 5х5. Получить новую матрицу
путем деления всех элементов данной матрицы на ее наибольший по
модулю элемент.

"""
from random import randint as rd

matrix = [[rd(-100, 100) for x in range(5)] for y in range(5)]
new_matrix = []

max_num = 1
for x in range(5):
    for y in range(5):
        if max_num < abs(matrix[x][y]):
            max_num = abs(matrix[x][y])

new_matrix = [[matrix[x][y] // max_num for x in range(5)] for y in range(5)]
print(new_matrix)



