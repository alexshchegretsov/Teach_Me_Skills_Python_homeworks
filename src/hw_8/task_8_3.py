"""
Рассчитать значение х определив и использовав необходимую функции.

x = (5**(1/2) + 5)/2 + (12**(1/2) + 12)/2 + (19**(1/2) + 19)/2

"""


def template(num: int) -> float:
    """Returns the sum of the number itself and its square root, divided by 2"""
    return (num ** (1 / 2) + num) / 2


def all_summ(num=5) -> float:
    """Returns the sum of template functions with increment by 7"""
    return template(num) + template(num + 7) + template(num + 14)


x = all_summ()
print(x)

