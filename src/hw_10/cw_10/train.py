def read_file():
    my_file = open('hw_10.txt')
    print(my_file.readline(), end='')
    print(my_file.readline(), end='')
    print(my_file.readline(), end='')
    print(my_file.readline(), end='')
    print(my_file.readline(), end='')
    print(my_file.readline(), end='')
    my_file.close()


def string_reading():
    my_file = open('hw_10.txt')
    while True:
        line = my_file.readline().strip()
        if not line:
            break
        print(line)
    my_file.close()


def print_first_str():
    my_file = open('hw_10.txt')
    i = 1
    while i:
        line = my_file.readline().strip()
        if i == 1:
            print(line)
            break
        i += 1
    my_file.close()


def print_fifth_str():
    my_file = open('hw_10.txt')

    i = 1
    while i:
        line = my_file.readline().strip()
        if i == 5:
            print(line)
            break
        i += 1
    my_file.close()


def first_five_str():
    my_file = open('hw_10.txt')
    i = 1
    while i < 6:
        line = my_file.readline().strip()
        print(line)
        i += 1
    my_file.close()


def from_3_to_7_str():
    my_file = open('hw_10.txt')
    i = 1
    while i:
        line = my_file.readline().strip()
        if i == 8:
            break
        elif i >= 3:
            print(line)
        i += 1
    my_file.close()


def print_all():
    my_file = open('hw_10.txt')
    i = 1
    while i:
        line = my_file.readline().strip()
        if not line:
            break
        print(line)
        i += 1
    my_file.close()


def main():
    print_all()
    # from_3_to_7_str()
    # first_five_str()
    # print_fifth_str()
    # print_first_str()
    # read_file()
    # string_reading()


if __name__ == '__main__':
    main()
