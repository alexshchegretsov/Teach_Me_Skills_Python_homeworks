"""
Имеется текстовый файл.
Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.
"""


def write_file_zero_to_one():
    """Function copies the text and replaces all zeros with units in it"""
    with open('hw_10.txt') as my_file:
        with open('new_file.txt', 'w') as new:
            [new.writelines(my_file.readline.replace('0', '1')) for my_file.readline in my_file]


def write_file_one_to_zero():
    """Function copies the text and replaces all units with zeros in it"""
    with open('new_file.txt') as my_file:
        with open('hw_10.txt', 'w') as new:
            [new.writelines(my_file.readline.replace('1', '0')) for my_file.readline in my_file]


def main():
    write_file_zero_to_one()
    write_file_one_to_zero()


if __name__ == '__main__':
    main()
