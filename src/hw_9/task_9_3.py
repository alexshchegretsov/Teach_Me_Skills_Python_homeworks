"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.

"""

def checker(func):
    def wrapper(*args, **kwargs):
        args = [x for x in args if x % 2]
        result = func(*args, **kwargs)
        return result

    return wrapper


@checker
def accept_list(*args: int) -> None:
    """Function accept and print list"""
    print(args)


accept_list(*[x for x in range(9)])
