"""
Ввести почтовый адрес.
Проверить доменной имя.
В случае если оно gmail.com, вывести на экран имя почтового ящика.
Иначе вывести надпись “DOMAIN NAME is not supported’

"""
email = input('Enter your email address:\t')
list_email = email.split('@')
if 'gmail.com' in list_email:
    print(f'{list_email[0]}')
else:
    print('DOMAIN NAME is not supported')
