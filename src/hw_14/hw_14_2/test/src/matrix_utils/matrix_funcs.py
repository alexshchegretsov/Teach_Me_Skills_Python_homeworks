from matrix_classes import Matrix


def max_matrix(obj: Matrix) -> int:
    """Return max element in 2-d matrix"""
    return max([item for row in obj.data for item in row])


def min_matrix(obj: Matrix) -> int:
    """Return min element in 2-d matrix"""
    return min([item for row in obj.data for item in row])


def summ_matrix(obj: Matrix) -> int:
    """Return sum of all elements in 2-d matrix"""
    return sum([item for row in obj.data for item in row])
