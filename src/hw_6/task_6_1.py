"""
Написать программу, в которой вводятся два операнда Х и Y и
знак операции sign (+, –, /, *). Вычислить результат Z в зависимости от знака.
Предусмотреть реакции на возможный неверный знак операции,
а также на ввод Y=0 при делении.
Организовать возможность многократных вычислений
без перезагрузки программа (т.е. построить бесконечный цикл).
В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').

"""

while True:
    X = int(input('enter first operand --->\t'))
    Y = int(input('enter second operand --->\t'))
    sign = input('enter 0 to quite\nenter operator --->\t')

    if sign == '/' and not Y:
        print('Zero division Error!')
        continue

    elif sign == '/' and Y:
        print(f'{X} {sign} {Y} = {X/Y}')
        continue

    elif sign not in ['-', '+', '*', '/', '0']:
        print(f'{sign} is invalid operator!')
        continue

    elif sign == '0':
        break

    operation = {'-': X - Y, '+': X + Y, '*': X * Y}
    print(f'{X} {sign} {Y} = {operation[sign]}')

