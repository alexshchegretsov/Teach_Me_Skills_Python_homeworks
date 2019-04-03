"""
Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.

"""
from datetime import timedelta

trains = [
    {
        'number': 52,
        'departure': 'Minsk',
        'departure_time': [7, 2],
        'destination': 'Grodno',
        'destination_time': [11, 48]
    },
    {
        'number': 62,
        'departure': 'Moscow',
        'departure_time': [3, 12],
        'destination': 'Prague',
        'destination_time': [21, 39]  # 18 ч 27 мин в пути
    },
    {
        'number': 72,
        'departure': 'Minsk',
        'departure_time': [0, 26],
        'destination': 'Munich',
        'destination_time': [22, 1]  # 22 ч 35 мин
    }
]

# Initialize result
long_distance_trains = []

# Initialize boundary for sorting
time_limit = timedelta(hours=7, minutes=20)

for train in trains:

    # Traverse through a particular dictionary
    # and looking for keys which containing time
    for key, v in train.items():
        if key == 'departure_time':
            dep = v
        elif key == 'destination_time':
            dest = v

            # Calculate the time difference
            diff = timedelta(hours=dest[0], minutes=dest[1]) - timedelta(hours=dep[0], minutes=dep[1])

    if diff > time_limit:
        long_distance_trains.append(train)

print(long_distance_trains)
