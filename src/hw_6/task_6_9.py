"""
Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.

"""
import datetime

trains = [
    {
        'number': 52,
        'departure': 'Minsk',
        'departure_time': '',
        'destination': 'Warsaw',
        'destination_time': ''
    },
    {
        'number': 62,
        'departure': 'Tallin',
        'departure_time': '',
        'destination': 'Prague',
        'destination_time': ''
    },
    {
        'number': 72,
        'departure': 'Nantes',
        'departure_time': '17:00',
        'destination': 'Rome',
        'destination_time': ''
    }
]
