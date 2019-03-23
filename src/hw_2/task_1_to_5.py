def task_1(a, b):
    print(a + b)
    print(a - b)
    print(a * b)


task_1(2, 5)


def task_2(x, y):
    operation = (abs(x) - abs(y))/(1 + abs(x*y))
    print(operation)


task_2(3, 2)


def task_3(z):
    V = z**3
    print(V)
    S = z**2*4
    print(S)


task_3(7)


def task_4(c, d):
    average = (c + d) / 2
    print(average)
    geometric_mean = (c * d) ** 0.5   # or pow() or math.sqrt() (sqrt more faster)
    print(geometric_mean)


task_4(4, 8)


def task_5(e, f):
    hypotenuse = pow((e**2 + f**2), 0.5)
    print(hypotenuse)


task_5(4, 4)
