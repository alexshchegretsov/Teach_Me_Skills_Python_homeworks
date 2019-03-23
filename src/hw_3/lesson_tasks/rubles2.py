"""
****************************************************************************************************
Получить на ввод количество рублей и копеек и вывести в правильной форме,
например, 3 рубля, 1 рубль 25 копеек, 3 копейки
****************************************************************************************************
First of all we are need to find all possible pairs and then to describe condition for each of them:
        1. рубль - копейка
        2. рубль - копеек
        3. рубль - копейки
        4. рубля - копейка
        5. рубля - копеек
        6. рубля - копейки
        7. рублей - копейка
        8. рублей - копеек
        9. рублей - копейки
"""
ruble = input('Введите количество рублей:\t')
cent = input('Введите количество копеек:\t')
if ruble.isdigit() and int(ruble) >= 0 and cent.isdigit() and int(cent) >= 0:
    last_char_ruble = int(ruble[-1])
    if len(ruble) >= 2:
        pre_last_char_ruble = int(ruble[-2])
    last_char_cent = int(cent[-1])
    if len(cent) >= 2:
        pre_last_char_cent = int(cent[-2])
    if (int(ruble) == 1 or (last_char_ruble == 1 and pre_last_char_ruble != 1)) and \
            (int(cent) == 1 or (last_char_cent == 1 and pre_last_char_cent != 1)):  # the number itself, not last char
        print(f'{ruble} рубль {cent} копейка')
    elif (int(ruble) == 1 or (last_char_ruble == 1 and pre_last_char_ruble != 1)) and \
            (last_char_cent == 0 or 5 <= last_char_cent <= 9 or (0 <= last_char_cent <= 9 and pre_last_char_cent == 1)):
        print(f'{ruble} рубль {cent} копеек')
    elif (int(ruble) == 1 or (last_char_ruble == 1 and pre_last_char_ruble != 1)) and \
            (2 <= last_char_cent <= 4 or (2 <= last_char_cent <= 4 and pre_last_char_cent != 1)):
        print(f'{ruble} рубль {cent} копейки')

    elif (2 <= last_char_ruble <= 4 or (2 <= last_char_ruble <= 4 and pre_last_char_ruble != 1)) and \
            (int(cent) == 1 or (last_char_cent == 1 and pre_last_char_cent != 1)):  # the number itself, not last char
        print(f'{ruble} рубля {cent} копейка')
    elif (2 <= last_char_ruble <= 4 or (2 <= last_char_ruble <= 4 and pre_last_char_ruble != 1)) and \
            (last_char_cent == 0 or 5 <= last_char_cent <= 9 or (0 <= last_char_cent <= 9 and pre_last_char_cent == 1)):
        print(f'{ruble} рубля {cent} копеек')
    elif (2 <= last_char_ruble <= 4 or (2 <= last_char_ruble <= 4 and pre_last_char_ruble != 1)) and \
            (2 <= last_char_cent <= 4 or (2 <= last_char_cent <= 4 and pre_last_char_cent != 1)):
        print(f'{ruble} рубля {cent} копейки')

    elif (last_char_ruble == 0 or 5 <= last_char_ruble <= 9 or
          (0 <= last_char_ruble <= 9 and pre_last_char_ruble == 1)) and \
            (int(cent) == 1 or (last_char_cent == 1 and pre_last_char_cent != 1)):  # the number itself, not last char
        print(f'{ruble} рублей {cent} копейка')
    elif (last_char_ruble == 0 or 5 <= last_char_ruble <= 9 or
          (0 <= last_char_ruble <= 9 and pre_last_char_ruble == 1)) and \
            (last_char_cent == 0 or 5 <= last_char_cent <= 9 or (0 <= last_char_cent <= 9 and pre_last_char_cent == 1)):
        print(f'{ruble} рублей {cent} копеек')
    elif (last_char_ruble == 0 or 5 <= last_char_ruble <= 9 or
          (0 <= last_char_ruble <= 9 and pre_last_char_ruble == 1)) and \
            (2 <= last_char_cent <= 4 or (2 <= last_char_cent <= 4 and pre_last_char_cent != 1)):
        print(f'{ruble} рублей {cent} копейки')
