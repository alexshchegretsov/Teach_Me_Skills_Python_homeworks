"""
Получить сумму кубов первых n натуральных чисел
"""
# num = int(input('enter:'))
# sum = 0
# while num:
#     print(num)
#     sum += num**3
#     num -= 1
# print(sum)

# 5_2
# import random
# from random import randint
# while True:
#     a = randint(0, 10)
#     print(a)
#     if a == 7:
#         print(a)
#         break

# 5_3

# n = int(input('enter n:\t'))
# m = int(input('enter m:\t'))
# sum = 0
# for i in range(n, m + 1):
#     sum += i ** 3
# print(sum)

# 5_4
#
# n = int(input('enter n:\t'))
# m = int(input('enter m:\t'))
# amount = 0
# for i in range(n, m + 1):
#     print(i)
#     amount += 1                 # or amount = m - n
# print(f'amount is {amount}')

# 5_5
import random
from random import randint
num = 5
matrix = []
for i in range(num):
    row = []
    for j in range(num):
        row.append(randint(1, 9))
    matrix.append(row)

for i in range(num):
    print(matrix[i])
    #  print(' '.join(matrix[i]))


summ = 0
for x in range(num):
    for j in range(num):
        if not matrix[x][j] % 3:
            summ += matrix[x][j]
print(summ)


