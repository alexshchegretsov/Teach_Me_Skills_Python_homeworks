"""
Написать функцию принимающая на вход неопределенное количество аргументов и
именованный аргумент mean_type. В зависимости от mean_type вернуть
среднеарифметическое либо среднегеометрическое.
Написать программу в виде трех функций.

"""
from random import randint as rd


def arithmetic_average(*args) -> float:
    """Returns arithmetic average of given list"""
    return sum(args) / len(args)


def geometric_average(*args) -> float:
    """Returns geometric average of given list"""

    total_multiply = 1
    for num in args:
        total_multiply *= num
    return total_multiply ** (1 / len(args))


def arithmetic_or_geometric(*args, mean_type='geom') -> float:
    """Returns arithmetic average or geometric.

    Depending on the mean_type value 'arith' or 'geom'
    the corresponding functions are called.

    Parameters
    ----------
    *args
        Any integers with any list length.
    mean_type: str
        By default calls geometric_average function.
        Can take value 'arith'.

    Returns
    ----------
    float
        geometric_average(*args) or arithmetic_average(*args)

    """
    return arithmetic_average(*args) if mean_type == 'arith' else geometric_average(*args)


seq = [rd(-30, 30) for x in range(5)]
print(arithmetic_or_geometric(*seq))
