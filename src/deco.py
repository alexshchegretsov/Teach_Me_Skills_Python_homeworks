from random import randint as rd
from datetime import datetime

# def time_is(func):
#     def wrapper(*args):
#         args = list(args)
#         start = datetime.now()
#         print(start)
#         func(*args)
#         print(datetime.now() - start)
#         return func
#
#     return wrapper


# @time_is
# def insertion_sort(*args):
#     args = list(args)
#     for index in range(1, len(args)):
#         while index and args[index - 1] > args[index]:
#             args[index - 1], args[index] = args[index], args[index - 1]
#             index -= 1
#     return args
#
#
# A = [rd(-20, 20) for x in range(30)]
# print(insertion_sort(*[rd(-20, 20) for x in range(30)]))

# def descending_insertion_sort(*args):
#     args = list(args)
#     for index in range(1, len(args)):
#         while index and args[index - 1] < args[index]:
#             args[index - 1], args[index] = args[index], args[index - 1]
#             index -= 1
#     return args
#
# print(descending_insertion_sort(*[rd(0,3) for x in range(10)]))


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


# nums = [1, 1, 2, 3, 3]


def sort():
    if not len(nums):
        return 0
    i = 0
    length = len(nums)
    for j in range(1, length):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]




# while i < length-1:
#     print(nums)
#     while j < length-1 and nums[i] == nums[j]:
#         j += 1
#     nums[i+1] = nums[j]
#     i += 1
# for i in range(length-1):
#     if nums[i] < nums[i+1]:
#         count += 1
# print(count)
