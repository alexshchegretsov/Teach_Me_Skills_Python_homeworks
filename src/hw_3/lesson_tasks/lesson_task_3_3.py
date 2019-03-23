"""
Ввести предложение.
Если число символов в предложении кратно 3 - добавить ! к концу строки.
Вывести строку на экран

"""
any_sent = input('Enter any sentence:\n')
if len(any_sent) % 3 == 0:
    exclaim_sent = f'{any_sent}!'
    print(exclaim_sent)
else:
    print(any_sent)
