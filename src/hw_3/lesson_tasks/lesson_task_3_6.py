"""
Ввести строку с клавиатуры
Если длина строки больше 5 - вывести значение на экран
Если длина строки меньше 5 - вывести строку “Need more!”
Если длина строки равна 5 - вывести строку “It is five”

"""
string = input('Enter anything: ')
if len(string) > 5:
    print(len(string))
elif len(string) < 5:
    print('Need more and more!')
elif len(string) == 5:
    print("Yep, it's five!")
