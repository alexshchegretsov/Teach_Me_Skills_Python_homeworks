"""
Создать программу для работы с  учетными записями пользователей.
Программа позволяет создавать, искать, править, фильтровать, удалять.
Учетная запись пользователя представляет из себя словарь со следующими данными:
имя, фамилия, дата рождения, профессия, числовой идентификатор(id).
Для хранения данных использовать json файл. Задание выполнить в отдельной папке.

"""

from functions import (
    menu,
    read_db,
    write_db,
    create_user,
    delete_user,
    show_n_users,
    search_user,
    edit_user,
    filter_by_keyword,
    choose_operation,
)


def main():
    while True:
        menu()
        operation = choose_operation()
        if not operation:
            break
        elif operation == 1:
            write_db(create_user())
        elif operation == 2 and read_db():
            delete_user()
        elif operation == 3 and read_db():
            show_n_users()
        elif operation == 4 and read_db():
            search_user()
        elif operation == 5 and read_db():
            edit_user()
        elif operation == 6 and read_db():
            filter_by_keyword()


if __name__ == '__main__':
    main()
