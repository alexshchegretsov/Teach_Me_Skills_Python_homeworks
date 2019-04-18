from random import randint as rd
a = [rd(-10,100) for _ in range(10)]
print(a)
for i in range(len(a)):
    while i > 0 and a[i-1] > a[i]:
        a[i-1],a[i] = a[i], a[i-1]
        i -= 1
print(a)