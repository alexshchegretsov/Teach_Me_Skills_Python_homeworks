from random import randint as rd


class Matrix:
    def __init__(self, data=None):
        self.data = data if data else [[rd(0, 9) for x in range(5)] for x in range(5)]
        self.n = len(self.data[0])
        self.m = len(self.data)

    def __str__(self):
        [print(' '.join(row_to_print)) for row_to_print in [map(str, row) for row in self.data]]
        return ''

    def max_matrix(self):
        return max([item for row in self.data for item in row])

    def min_matrix(self):
        return min([item for row in self.data for item in row])

    def summ_matrix(self):
        return sum([item for row in self.data for item in row])
