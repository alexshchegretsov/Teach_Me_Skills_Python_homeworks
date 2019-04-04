from random import randint as rd

def create_matrix(n):
    matrix = [[rd(-10, 10) for y in range(n)] for x in range(n)]
    return matrix


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


def max_matrix(matrix):
    """At the entrance takes a matrix and return largest element"""
    max_number = max(matrix[0])
    for row in matrix:
        if max_number < max(row):
            max_number = max(row)
    return max_number



def min_matrix(matrix):
    """At the entrance takes a matrix and return smallest element"""
    min_number = min(matrix[0])
    for row in matrix:
        if min_number < min(row):
            min_number = min(row)
    return min_number
