"""
Создать список с фамилиями.
Вывести все фамилии, которые начинаются на П и заканчиваются на а

"""
last_name = ['Посуда', 'Пушкинова', 'Птица', 'Толстая', 'Достоевская']
for name in last_name:
    if name[0].lower() == 'п' and name[-1] == 'а':
        print(name)



    # if ord(name[0].lower()) == 1087 and ord(name[-1]) == 1072:
    #     print(name)