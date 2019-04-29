class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return eval(f'{self.x} + {self.y}')

    def substraction(self):
        return eval(f'{self.x} - {self.y}')

    def multiply(self):
        return eval(f'{self.x} * {self.y}')

    def division(self):
        return eval(f'{self.x} / {self.y}')


