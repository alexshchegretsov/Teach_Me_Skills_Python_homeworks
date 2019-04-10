# A = ['savghkh', 'whellloo', 'sdgk', 'sjdkt']
# new_list = [i[::-1] for i in A]
# print(new_list)


# def hello(*args):
#     return [f'Hello {name}' for name in args if 'x' in name]
#
# A = ['alice', 'alex']
# print(hello(*A))

"""
Дан список словарей. Каждый словарь описывает машину(серийный номер и год выпуска).
Создать новый список со всеми машинами, год выпуска которых больше n


"""
# car_list = [
#     dict(number='01', year='1991'),
#     dict(number='02', year='1992'),
#     dict(number='03', year='1993'),
#     dict(number='04', year='1994'),
#     dict(number='05', year='1995')
# ]
# print(car_list)
# new_car_list = [car for car in car_list if int(car['year']) < 1993]
# print(new_car_list)
# n = 0
# for car in car_list:
#     if car['year'] > n:

#         pass

# old_dict = {'aaa': 1, 'rtwe': 2}
# new_dct = {key + str(len(key)): value for key, value in old_dict.items()}
# print(new_dct)


# old_dict = {'aaa': 1, 'rtwe': 2}
# new_dict = {value: key for key, value in old_dict.items()}
# print(new_dict)

# lambda
# print((lambda name: f'{name} Hello')('alex'))


# B =  (lambda names: [f'{name} Hello' for name in names])(['alex'])
# print(B)

# decorators
# def my_decorator(func):
#     def wrapper():
#         print('start')
#         func()
#         print('finish')
#     return wrapper()
#
# @my_decorator
# def my_func():
#     print('wetlhld')
#
from datetime import datetime
import functools
