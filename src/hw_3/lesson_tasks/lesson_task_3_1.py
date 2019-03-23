"""
Ввести с клавиатуры имя пользователя.
Вывести на экран “Hello, name!”
Вывести на экран зеркальное отображение полученной строки

"""
full_name = input('Enter your full name:\t')
sent = f'Hello {full_name.title()}'
print(sent)
print(sent[::-1])
