from random import randint as rd


class Matrix:
    """Create and represent 2-d matrix"""

    def __init__(self, data=None):
        """initializes a two-dimensional matrix and,
        in the absence of dimensions, sets a default size of 5x5
        with random numbers from 0 to 9"""
        self.data = data if data else [[rd(0, 9) for x in range(5)] for x in range(5)]
        self.n = len(self.data[0])
        self.m = len(self.data)

    def __str__(self):
        [print(' '.join(row_to_print)) for row_to_print in [map(str, row) for row in self.data]]
        return ''
