"""
Вычислить квадратное уравнение ax2 + bx + c = 0 (*)
D = b2 – 4ac;
x1,2 = (-b +/- sqrt (D)) / 2a
Предусмотреть 3 варианта:
Два действительных корня
Один действительный корень
Нет действительных корней

"""
# a*x**2 + b*x + c = 0


def finding_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant == 0:
        x = (-b) / 2*a
        return f'One root, x = {x}'
    elif discriminant > 0:
        x_1 = ((-b) + discriminant ** 0.5) / 2*a
        x_2 = ((-b) - discriminant ** 0.5) / 2*a
        return f'Two roots, x_1 = {x_1}, x_2 = {x_2}'
    else:
        return 'No roots founds here'


quadratic_equation = finding_roots(0, 0, 0)
print(quadratic_equation)
