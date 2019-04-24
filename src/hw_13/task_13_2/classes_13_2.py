class ValueError(Exception):
    def __init__(self, message="pages can't be negative"):
        super().__init__(message)


class SyntaxTerribleError(Exception):
    def __init__(self, message="this book from future"):
        super().__init__(message)


class HorrorError(Exception):
    def __init__(self, message="It's your LAST error ever"):
        super().__init__(message)


class HomelessError(Exception):
    def __init__(self, message="homeless people like to read books, but for such money he may steal it"):
        super().__init__(message)


class Book:
    def __init__(self, *args):
        if args[0] < 0:
            raise ValueError
        elif args[1] > 2020:
            raise SyntaxTerribleError
        elif args[2] == 'Stephen King':
            raise HorrorError
        elif args[3] > 100:
            raise HomelessError
        self.pages = args[0]
        self.year = args[1]
        self.author = args[2]
        self.price = args[3]
