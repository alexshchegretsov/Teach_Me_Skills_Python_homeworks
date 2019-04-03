"""
Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300.

"""
from time import time
print(time())
m = 200
n = 300
matrix = []

for main_number in range(m, n + 1):
    row = []
    matrix.append(row)
    for current_number in range(1, main_number // 2 + 1):
        if not main_number % current_number:
            row.append(current_number)

for i, number_dividers in enumerate(matrix):
    for j in range(m, n + 1):
        if sum(number_dividers) == j and sum(matrix[j - m]) == (i + m):
            print(f'{j} and {i + m} are friendly numbers')
print(time())



