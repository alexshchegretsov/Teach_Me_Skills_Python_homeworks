
from datetime import datetime


def main_decorator(func : 'any function'):
    def decorator_1(*args):
        start = datetime.now()
        func()
        print(datetime.now() - start)
        return func

    return decorator_1



def got_bucks(word):
    return f"I've got {word}"


print(main_decorator(got_bucks)('10$'))
