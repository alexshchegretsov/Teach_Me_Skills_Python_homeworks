"""
Описать функцию is_power_n( k , n ) логического типа,
возвращающую True, если целый параметр k (> 0) является степенью числа n (> 1),
и False в противном случае.

Дано число n (> 1) и набор из 10 целых положительных чисел.
С помощью функции is_power_n найти количество степеней числа N в данном наборе.

"""
from random import randint as rd


def is_power_n(k, n: int) -> bool:
    """Returns True or False depending on whether the k is a power of n.

    if k is divisible by n and eventually
    there will be 1, then k is a power of n.

    Parameters
    ----------
    k: int
        k > 0, the number that we check is the power of n.
    n: int
        Control number itself.

    Return
    ----------
    bool
        True if k is a power of n, False otherwise.
    """
    while True:
        if k == 1:
            return True
        elif k < 1:
            return False
        k /= n


def power_amount(n: int, *args) -> int:
    """Returns the number of powers of a number in a given list.
    
    Parameters
    ----------
    n: int
        Control number itself.
    args
        Positive integers with any list length.

    Return
    ----------
    int
        Amount of numbers which are powers of the given number.
    """
    amount = 0
    for num in args:
        if is_power_n(num, n):
            amount += 1
    return amount


A = [rd(1, 100) for _ in range(20)]
print(A, power_amount(2, *A))
