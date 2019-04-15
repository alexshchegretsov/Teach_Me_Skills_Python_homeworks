"""
Имеется текстовый файл.
Все четные строки этого файла записать во второй файл,
а нечетные — в третий файл. Порядок следования строк сохраняется.
"""


def even_odd_strings():
    """Writes odd and even lines to different files with order preservation"""
    with open('hw_10.txt') as my_file:
        with open('even.txt', 'w') as even:
            with open('odd.txt', 'w') as odd:

                i = 1
                while i:
                    line = my_file.readline()
                    if not line:
                        break
                    elif not i % 2:
                        even.writelines(line)
                        odd.writelines('\n')
                        i += 1
                        continue

                    odd.writelines(line)
                    even.writelines('\n')
                    i += 1


def main():
    even_odd_strings()


if __name__ == '__main__':
    main()
