from datetime import datetime


# decorators


def timeit(arg):
    print(arg)

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result

        return wrapper

    return outer


@timeit('fk')
def create_list_for(n):
    l = []
    for i in range(n):
        if not i % 2:
            l.append(i)
    return l


@timeit('name')
def create_list_gen(n):
    l = [x for x in range(n) if not x % 2]
    return l
