"""
Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 ->  2 3 4 5 1

"""
sequence_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sequence_2 = []
length = len(sequence_1)
i = 0
while i < length:
    add_num = sequence_1[i + 1]
    sequence_2.append(add_num)
    if i == length - 2:
        add_first_num = sequence_1[0]
        sequence_2.append(add_first_num)
        break
    i += 1
print(sequence_2)

