"""
Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы, превосходящих
среднее арифметическое значение элементов матрицы и
сумма индексов которых четна.
"""
from random import randint as rd

m = 7
n = 4
matrix = []

summ = 0
for x in range(n):
    row = []
    matrix.append(row)
    for y in range(m):
        numb = rd(0,9)
        row.append(numb)
        summ += numb
average = summ / (m*n)

count = 0
for i, row in enumerate(matrix):
    for j, elem in enumerate(row):
        if elem > average and not (i + j) % 2:
            count += 1
print(count)
