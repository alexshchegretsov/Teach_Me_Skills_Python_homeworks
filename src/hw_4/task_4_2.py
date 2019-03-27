"""
Дан список целых чисел. Подсчитать сколько четных чисел в списке

"""
nums = [4, 6, 19, 55, 1002, 11, 74, 88, 2]
even_nums = 0
i = 0
length = len(nums)
while i < length:
    if nums[i] % 2 == 0:   # if not nums[i] % 2:
        even_nums += 1
    i += 1
print(even_nums)
