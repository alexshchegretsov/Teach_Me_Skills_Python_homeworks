"""
Создать универсальный декоратор, который меняет
порядок аргументов в функции на противоположный.
"""


def reverser(func):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        result = func(*args, **kwargs)
        return result

    return wrapper


@reverser
def counter(*args):
    args = list(args)
    for i in range(len(args)):
        args[i] *= 2
    return args


print(counter(*[1, 2]))
