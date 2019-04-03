"""
Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего).

"""
from random import randint as rd

seq = [rd(-10, 30) for i in range(15)]

list_length = len(seq)
sub_list_length = 1
count = 0

for i in range(list_length - 1):

    if seq[i + 1] > seq[i]:
        sub_list_length += 1
    elif sub_list_length > 1:
        count += 1
        sub_list_length = 1

if sub_list_length > 1:
    count += 1

print(f'{seq}\n{count}')

# Exactly the same, but "while"-ish

# while i < list_length-1:
#
#     if seq[i+1] > seq[i]:
#         sub_list_length += 1
#         i += 1
#     elif sub_list_length > 1:
#             count += 1
#             i += 1
#             sub_list_length = 1
#
# if sub_list_length > 1:
#     count += 1
