"""
Имеются два текстовых файла с одинаковым числом строк.
Выяснить, совпадают ли их строки.
Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга.
"""


def compare_strings() -> int:
    """Function compares two files line by line and
    displays the line number of the first nonconformity"""
    with open('odd.txt') as first_file:
        with open('even.txt') as second_file:

            second_list = second_file.readlines()
            for i, line in enumerate(first_file):
                if line != second_list[i]:
                    return i + 1


def main():
    compare_strings()


if __name__ == "__main__":
    main()
