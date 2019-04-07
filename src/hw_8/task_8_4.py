"""
Написать функцию по решению квадратных уравнений.

a*x**2 + b*x + c = 0
D = b**2 - 4*a*c

"""
from typing import Union


def discriminant(a, b, c: Union[int, float]) -> Union[int, float]:
    """Returns discriminant of appropriate equation with given numbers"""
    return b ** 2 - 4 * a * c


def one_root(a, b: Union[int, float]) -> float:
    """Returns root of quadratic equation when discriminant == 0"""
    return (-b) / (2 * a)


def first_root_of_two(a, b, c: Union[int, float]) -> float:
    """Returns first root of quadratic equation when discriminant > 0"""
    return ((-b) + discriminant(a, b, c) ** 0.5) / (2 * a)


def second_root_of_two(a, b, c: Union[int, float]) -> float:
    """Returns second root of quadratic equation when discriminant > 0"""
    return ((-b) - discriminant(a, b, c) ** 0.5) / (2 * a)


def quadratic_equation(a, b, c: Union[int, float]) -> Union[float, str, tuple]:
    """Returns the corresponding result by first solving a quadratic equation.

    Depending on the sign of discriminant,
    the quadratic equation can have two, one, or none of the roots.
    Consider all three cases.

    1st case.
    If discriminant > 0 - we are have two roots.

    2nd case.
    If discriminant = 0 - we are have only one root.

    3rd case.
    If discriminant < 0 - we are have no roots.

    Parmeters
    ----------
    a: int, float
        First multiplier.
    b: int, float
        Second multiplier.
    c: int, float
        Third multiplier.

    Return
    ----------
    float
        Returns one root if discriminant = 0.
    float, tuple
        Returns two roots if discriminant > 0.
    str
       Returns 'No roots founds here' if discriminant < 0.
    """
    if not discriminant(a, b, c):
        return one_root(a, b)
    elif discriminant(a, b, c) > 0:
        return first_root_of_two(a, b, c), second_root_of_two(a, b, c)
    else:
        return 'No roots founds here'


print(quadratic_equation(5, 7, 1))
