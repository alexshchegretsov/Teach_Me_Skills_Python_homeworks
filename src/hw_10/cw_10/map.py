"""
Дан список чисел. Вернуть список, где каждый число переведено в строку
[5, 3] -> [‘5’, ‘3’]

"""
import statistics
from random import randint as rd
from functools import reduce
result = list(map(str, [1, 2, 3]))

temps = [("Berlin", 29), ("Cairo", 32), ('Beijing', 17), ("Paris", 22),
         ("Moscow", 14), ("Minsk", 18), ("Tokyo", 27)]
c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)

# print(list(map(c_to_f, temps)))

data = [-1.4, 2.0, 0.6, -1.1, -0.7, 4.0, 2.9]
avg = statistics.mean(data)

print(list(filter(lambda x: x > avg, data)))
print(list(filter(lambda x: x < avg, data)))

countries = ['', 'Argentina', 'Brazil', '', 'Ecuador', 'Mexico', '', '']
print(list(filter(None, countries)))

data = [x for x in range(1, 11)]
multiplier = lambda x, y: x * y
print(reduce(multiplier,data))

product = 1
for x in range(1, 11):
    product *= x

print(product)
