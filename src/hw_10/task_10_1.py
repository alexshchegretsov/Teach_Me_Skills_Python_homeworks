"""
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""


def writer():
    """Writes three lines at the end of the file that are entered from the keyboard"""
    with open('hw_10.txt', 'a') as my_file:
        [my_file.writelines(f'{input()}\n') for _ in range(3)]


def main():
    writer()


if __name__ == '__main__':
    main()
