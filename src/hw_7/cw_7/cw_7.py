# def hello(name):
#     print(f'Hello {name.title()}')
#
#
# hi = hello('Alex')
# print(hi)
#
# names = ['jessie', 'mr.white', 'john', 'andrew']
#
# for i in names:
#     hello(i)


# def fact(i):
#     result = 1
#     while i:
#         result *= i
#         i -= 1
#     return result
#
# print(fact(7))

from random import randint as rd
# first - import; second - from; then functions
def create_matrix(n):
    matrix = [[rd(-10, 10) for y in range(n)] for x in range(n)]
    return matrix

matrix = create_matrix(5)

def print_matrix(matrix):
    for i in matrix:
        print(i)

# printing = print_matrix(matrix)

def matrix_summ(matrix):
    summ = 0
    for row in matrix:
        for num in row:
            summ += num
    return summ

print(matrix_summ(matrix))

def max_matrix(matrix):
    """At the entrance takes a matrix and return largest element"""

    # Initialize element for comparing and
    # comparing with others find the maximum number
    max_number = max(matrix[0])
    for row in matrix:
        if max_number < max(row):
            max_number = max(row)
    return max_number

print(max_matrix(matrix))


def min_matrix(matrix):
    """At the entrance takes a matrix and return smallest element"""

    # Initialize element for comparing and
    # comparing with others find the minimum number
    min_number = min(matrix[0])
    for row in matrix:
        if min_number < min(row):
            min_number = min(row)
    return min_number

print(min_matrix(matrix))