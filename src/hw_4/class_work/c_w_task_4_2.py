"""
Просуммировать неопределенное количество чисел, вводимых пользователем,
суммировать до тех пор, пока пользователь не введёт слово «стоп»

"""
sum_all = 0
while True:
    num = input('Enter num or enter quit to end program:\t')
    if num.isdigit():
        number = int(num)
        sum_all += number
        continue
    elif num == 'quit':
        print(sum_all)
        break
    else:
        print('Enter incorrect')
        continue









