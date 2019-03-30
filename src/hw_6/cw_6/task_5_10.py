"""
Дан двухмерный массив n × m элементов.
Определить, сколько раз встречается число 7 среди элементов массива.

"""
from random import randint as rd
m = 7
n = 4
matrix = []
count = 0
for x in range(n):
    row = []
    matrix.append(row)
    for y in range(m):
        numb = rd(-10, 10)
        row.append(numb)

        if numb == 7:
            count += 1

print(count)

# Short version
m = 7
n = 4
matrix = [[rd(0, 9) for i in range(m)] for j in range(n)]
amount = 0
for row in matrix:
    amount += row.count(7)
print(amount)
