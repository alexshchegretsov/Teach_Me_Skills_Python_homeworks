"""
Для каждого натурального числа в промежутке от m до n
вывести все делители, кроме единицы и самого числа.
m и n вводятся с клавиатуры.
Пример:m =100, n = 105

100: 2 4 5 10 20 25 50
101:
102: 2 3 6 17 34 51
103:
104: 2 4 8 13 26 52
105: 3 5 7 15 21 35

"""
while True:
    m = input('---> m:\t').strip()
    n = input('---> n:\t').strip()
    if m.isdigit() and n.isdigit():
        m = int(m)
        n = int(n)

        for x in range(m, n + 1):
            printed_row = []
            for y in range(2, x):
                if not x % y:
                    printed_row.append(str(y))
            print(f'{x}: {" ".join(printed_row)}')
        break
    else:
        print('n and m must be a digit')
        continue

