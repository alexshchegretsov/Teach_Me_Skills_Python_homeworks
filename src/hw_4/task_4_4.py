"""
Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 ->  2 3 4 5 1

"""
# 1st var
sequence_1 = [1, 2, 3, 4, 5, 6]
# without while
reverse_seq_1 = sequence_1[::-1]
first_item = reverse_seq_1.pop()
normalize_seq = reverse_seq_1[::-1]
normalize_seq.append(first_item)
print(normalize_seq)

