seq = (-20, -5, 10, 15)
seq = list(seq)
sorted_seq = []
length = len(seq)
print(seq)

while length:

    id_minimum = 0
    for i in range(length):
        if abs(seq[id_minimum]) > abs(seq[i]):
            id_minimum = i
    sorted_seq.append(seq[id_minimum])
    seq.remove(seq[id_minimum])
    length = len(seq)

print(seq, sorted_seq)
