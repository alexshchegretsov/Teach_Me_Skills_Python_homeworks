"""
Ввести число, проверить на то, что было введено именно число.
Возвести его в куб.

"""
num = input('Enter any digit: ')
if num.isdigit():
    cube_num = int(num)**3
    print(cube_num)
