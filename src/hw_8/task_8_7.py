"""
Описать функцию fact2( n ) вещественного типа,
вычисляющую двойной факториал :n!! = 1·3·5·...·n, если n — нечетное;
n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа.
С помощью этой функции найти двойные факториалы пяти данных целых чисел
"""
from typing import Union


def factorial_1(number: Union[int, float]) -> int:
    """Returns factorial of given number"""
    total = 1
    while number:
        total *= number
        number -= 1
    return int(total)


def even(number: int) -> int:
    """Returns  double factorial of given even number"""
    return int(2 ** (number / 2) * factorial_1(number / 2))


def odd(number: int) -> int:
    """Returns double factorial of given odd number"""
    return int(factorial_1(number + 1) / even(number + 1))


def factorial_2(number: int) -> int:
    """Returns double factorial of odd or even number"""
    return even(number) if not number % 2 else odd(number)


# Можно и без этой функции, но с циклом в предыдущей
def printer(*args):
    """Print each number double factorial of given list"""
    for _ in args:
        print(factorial_2(_))


N = [3, 4, 7, 18]
printer(*N)
