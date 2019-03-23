# a*x**2 + b*x + c = 0
def quadratic_equation(a, b, c):
    def discr(a, b ,c):
         return   b**2 - 4*a*c
    if discriminant == 0:
        x = (-b) / 2*a
        print(f'One root, x = {x}')
    elif discriminant > 0:
        x_1 = ((-b) + discriminant ** 0.5) / 2*a
        x_2 = ((-b) - discriminant ** 0.5) / 2*a
        print(f'Two roots, x_1 = {x_1}, x_2 = {x_2}')
    else:
        print('No roots')


quadratic_equation(1, -2, -3)












