"""
Дан файл, содержащий различные даты.
Каждая дата - это число, месяц и год. Найти самую раннюю дату.
"""
import datetime
from random import choice


def generate_and_write_date():
    """Function emulates random dates and writes them to a file
    excluding the last days of months"""
    any_year = [_ for _ in range(1, 10000)]
    any_month = [_ for _ in range(1, 13)]
    any_day = [_ for _ in range(1, 28)]

    with open('dates.txt', 'w') as file:
        for _ in range(10):
            file.write(f'{datetime.date(choice(any_year), choice(any_month), choice(any_day))}\n')


def find_earliest_date():
    """Function finds and returns the earliest date"""
    with open('dates.txt') as file:
        date_list = file.readlines()
        return min(date_list)


def main():
    generate_and_write_date()
    find_earliest_date()



if __name__ == '__main__':
    main()
