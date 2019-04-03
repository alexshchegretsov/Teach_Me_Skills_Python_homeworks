"""
Дано число. Найти сумму и произведение его цифр.

"""
num = 12745459
summ = 0
mult = 1
num = list(str(num))
for x in num:
    summ += int(x)
    mult *= int(x)
print(summ, mult)
