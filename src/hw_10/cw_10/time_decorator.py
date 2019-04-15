"""
Написать декоратор, который будет выводить время выполнения функции

"""
from datetime import datetime


def timeit(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print(datetime.now() - start)
        return result

    return wrapper


@timeit
def cube(*args):
    args = [x ** 3 for x in args]
    return args


# print(timeit(cube)(*[x for x in range(10)]))
# print(cube(*[x for x in range(10)]))

def main():
    print(cube(*[x for x in range(10)]))

if __name__ == '__main__':
    main()
