"""
Создать универсальный декоратор, который меняет
порядок аргументов в функции на противоположный.
"""


def reverser(func):
    def wrapper(*args, **kwargs):
        args = list(args)[::-1]
        func(*args, **kwargs)
        return func

    return wrapper

