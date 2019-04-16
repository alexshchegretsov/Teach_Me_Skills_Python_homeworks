"""
Создать программу для работы с  учетными записями пользователей.
Программа позволяет создавать, искать, править, фильтровать, удалять.
Учетная запись пользователя представляет из себя словарь со следующими данными:
имя, фамилия, дата рождения, профессия, числовой идентификатор(id).
Для хранения данных использовать json файл. Задание выполнить в отдельной папке.

"""

import json
import datetime
from time import sleep


def menu():
    while True:
        try:
            with open('train_persons.json') as file:
                data = json.loads(file.read())
        except:
            data = []
        print('-' * 55)
        print('\t\t\t\t\t  MENU')
        print('enter the appropriate number to perform the operation')
        print('-' * 55)
        print("""
                1. Create user
                2. Delete user
                3. Show first n users
                4. Find user
                    """)
        print(f'{len(data)} users in database')
        print('-' * 55)
        print('For EXIT enter 0')
        print('-' * 55)
        operation = input('Enter operation >>>')

        if operation.isdigit() and 0 <= int(operation) <= 7:
            operation = int(operation)
            return operation
        else:
            print('Enter correct value from 0 to 7')
            sleep(3)
            continue


def create_user():
    f_name = input('Enter first name >>>').title()
    l_name = input('Enter last name >>>').title()
    b_year = int(input('Enter birth year >>'))
    b_month = int(input('Enter birth month >>'))
    b_day = int(input('Enter birth day >>'))
    b_date = str(datetime.date(b_year, b_month, b_day))
    prof = input('Enter profession >>>')
    identify = input('Enter id >>>')
    person = {
        'first_name': f_name,
        'last_name': l_name,
        'birth_date': b_date,
        'profession': prof,
        'id': identify
    }
    return person


def write_json(func):
    try:
        data = json.load(open('train_persons.json'))
    except:
        data = []
    data.append(func)
    with open('train_persons.json', 'w') as file:
        json.dump(data, file, indent=2)


def delete_user():
    while True:
        del_id = input('Enter user id you want to delete or 0 to BACK >>>')
        if del_id.isdigit() and not int(del_id):
            break
        elif del_id.isdigit():

            with open('train_persons.json') as file:
                data = json.loads(file.read())
                for i, x in enumerate(data):
                    if x['id'] == del_id:
                        del data[i]

                        with open('train_persons.json', 'w') as file_1:
                            json.dump(data, file_1, indent=2)
                            print('Operation completed correctly!')
                            sleep(2.5)
                            break
        else:
            print('No such id, enter correct id')
            sleep(3)
            continue


def show_n_users():
    while True:
        try:
            with open('train_persons.json') as file:
                data = json.loads(file.read())
                print(f'{len(data)} users availible')
                sleep(.5)
                amount = input('Enter amount or 0 to BACK >>>')
                print('\n')
                if amount.isdigit() and not int(amount):
                    break
                elif amount.isdigit() and int(amount) <= len(data):
                    amount = int(amount)
                    for i in range(amount):
                        for k, v in data[i].items():
                            print(f'{k}: {v}')
                        print('-' * 28)
                    decision = input('Enter 1 to continue, 0 to BACK in menu >>>')
                    if decision.isdigit() and not int(decision):
                        break
                    else:
                        continue
        except:
            print('0 users availible, database empty')
            sleep(2)
            break


def find_user():
    while True:
        with open('train_persons.json') as file:
            data = json.loads(file.read())
            name = input('Enter user name >>>')
            last_name = input('Enter last user name >>>')
            print('\n')
            if name.isalpha() and last_name.isalpha():
                name = name.title()
                last_name = last_name.title()
                for i, x in enumerate(data):
                    if x['first_name'] == name and x['last_name'] == last_name:
                        for k, v in data[i].items():
                            print(f'{k}: {v}')
                        break
                else:
                    print(f'There is no such user {name} {last_name}')
                    sleep(1.5)
                    decision = input('Enter 1 to continue, 0 to BACK in menu >>>')
                    if decision.isdigit() and not int(decision):
                        break
                    else:
                        continue
                # break
                decision = input('Enter 1 to continue, 0 to BACK in menu >>>')
                if decision.isdigit() and not int(decision):
                    break
                else:
                    continue

            else:
                print('Incorrect input, try again')
                sleep(2)
                continue


def main():
    while True:
        operation = menu()
        if not operation:
            break
        elif operation == 1:
            write_json(create_user())
            continue
        elif operation == 2:
            delete_user()
            continue
        elif operation == 3:
            show_n_users()
            continue
        elif operation == 4:
            find_user()
            continue


if __name__ == '__main__':
    main()
