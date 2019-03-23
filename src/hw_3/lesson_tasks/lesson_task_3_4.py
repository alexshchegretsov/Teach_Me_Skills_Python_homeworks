"""
Ввести предложение.
Если в предложении есть слово code - вывести на экран Yes, иначе вывети на экран No

"""
sent = input('Any sentence:\n')
if 'code' in sent:
    print('Yes')
else:
    print('No')
