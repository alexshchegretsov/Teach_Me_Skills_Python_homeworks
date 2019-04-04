"""
Написать 12 функций по переводу:

    Дюймы в сантиметры
    Сантиметры в дюймы
    Мили в километры
    Километры в мили
    Фунты в килограммы
    Килограммы в фунты
    Унции в граммы
    Граммы в унции
    Галлон в литры
    Литры в галлоны
    Пинты в литры
    Литры в пинты

Примечание: функция принимает на вход число и возвращает конвертированное число

"""
import conversion as cv
from time import sleep


functions = {
    1: cv.inchs_to_centimeters,
    2: cv.centimeters_to_inchs,
    3: cv.miles_to_km,
    4: cv.km_to_miles,
    5: cv.pounds_to_kilos,
    6: cv.kilos_to_pounds,
    7: cv.ounces_to_grams,
    8: cv.grams_to_ounces,
    9: cv.gallons_to_liters,
    10: cv.liters_to_gallons,
    11: cv.pints_to_liters,
    12: cv.liters_to_pints
}

units = {
    1: 'Inchs to centimeters',
    2: 'Centimeters to inchs',
    3: 'Miles to kilometers',
    4: 'Kilometers to miles',
    5: 'Pounds to kilograms',
    6: 'Kilograms to pounds',
    7: 'Ounces to grams',
    8: 'Grams to ounces',
    9: 'Gallons to liters',
    10: 'Liters to gallons',
    11: 'Pints to liters',
    12: 'Liters to pints'
}

while True:

    print('*' * 50)
    print('\n\t\t\tChoose conversion below\nand ENTER the appropriate number for the operation\n')
    print('*' * 50)

    # Display options
    for k, v in units.items():
        print(f'\t\t{k}.  {v}')
        sleep(.07)

    print('x' * 50)
    print('\t\t\tFor EXIT enter 0')
    print('x' * 50)
    sleep(1)
    operation = input('Enter operation number >>>\t')

    # Validation for exit
    if operation.isdigit() and not int(operation):

        print('---\t' * 13)
        print('\t\t\t\t\t Bye!')
        print('''
         _____
        ( bye )
         -----
                O   ^__^
                 o  (oo)\_______
                    (__)\       )\/*
                        ||----w |
                        ||     ||

        ''')
        print('  ---' * 10)
        break

    elif operation.isdigit() and 1 <= int(operation) <= 12:
        operation = int(operation)

        argument = input(f'Enter amount of {units[operation].split()[0].lower()} >>> ')
        if argument.isdigit():
            argument = int(argument)
            print(f'{functions[operation](argument)} {units[operation].split()[2].lower()}')
            sleep(4)
        else:
            continue
    else:
        print('Incorrect value!')
        continue