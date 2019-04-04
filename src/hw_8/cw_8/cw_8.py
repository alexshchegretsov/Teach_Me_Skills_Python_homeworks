from random import randint as rd
from matrix_utils import create_matrix as cm, print_matrix as pm
from typing import Union, List


# print(mx.create_matrix(9))
# def create_matrix(n,random_from=1,random_to=9):
#     matrix = [[rd(random_from, random_to) for y in range(n)] for x in range(n)]
#     return matrix
#
# output = create_matrix(6)
# print(output)

def summ_all(*args: List) -> int:
    """Returns sum of all elements each multiply on their own index in list"""

    result = 0
    for i, num in enumerate(args):
        result += i * num
    return result


print(summ_all(11, 7, 9, 45))

# Unpacking arguments with sign "*"
# arguments = [1, 2, 3, 4]
# print(summ_all(*arguments))

def my_func(a, b):
    summ = a + b
    diff = a - b
    return summ, diff  # return tuple

def sum_and_max(*args):
    return sum(args), max(args)

arguments = [1, 200, 11, 44, -79, 3]
a, b = sum_and_max(*arguments)   # how to unpack ??
print(sum_and_max(*arguments))



def show_even(**kwargs):
    for k, v in kwargs.items():
        if not len(k) % 2:
            print(k, v)

dictionary = {'ab': 4, 'a': 7, '0abscd': 5}

show_even(**dictionary)


def full_func(*args, **kwargs):
    print(args)
    print(kwargs)

full_func(1,2,3,a=4,b=5,c=6)