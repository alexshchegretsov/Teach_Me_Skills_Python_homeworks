'''
Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2

'''
# 1st var
list_1 = [1, 4, 17, 9, 7]
list_2 = []
reversed_list_1 = list_1[::-1]
length = len(reversed_list_1)
while length > 0:
    recoverable_item = reversed_list_1.pop()
    pluggable_item = recoverable_item*(-2)
    list_2.append(pluggable_item)
    length -= 1
print(list_2)

# 2nd var
# list_1 = [1, 4, 17, 9, 7]
# reversed_list = list_1[::-1]
# list_2 = []
# while True:
#     recoverable_item = reversed_list.pop()
#     pluggable_item = recoverable_item*(-2)
#     list_2.append(pluggable_item)
#     if len(reversed_list) == 0:
#         break
# print(list_2)

