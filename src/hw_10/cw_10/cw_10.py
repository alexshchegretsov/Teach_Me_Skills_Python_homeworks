from functools import reduce


# result = map(str, [5, 3])
# print(list(result))

# result = list(filter(lambda name: 'k' in name or 'K' in name, ['aleksey', 'alex']))
# print(result)

# вместо генератора попробовать filter
# result = reduce(lambda a, x: a * x, filter(lambda x: x % 3 == 0, [i for i in range(1, 20)]), 1)
# result = reduce(lambda a, x: a * x, [i for i in range(1, 20) if not i % 3], 1)
# print(result)
#
# summ = reduce(lambda a, x: a * x, [2, 3, 4])
# print(summ)
def open_file():
    # my_file = open('test.txt')
    # i = 5
    # while i:
    #     line = my_file.readline().strip()
    #     if i > 3:
    #         print(f'{line} ---> task g')
    #     i -= 1
    # else:
    #     print(f'{line} ---> task b')

    # i = 1
    # while i <= 5:
    #     line = my_file.readline().strip()
    #     if 1 < i < 5:
    #         print(line)
    #     i += 1

    # print(my_file.readlines())
    # with open('test.txt','w') as file:
    #
    #     for i in range(6):
    #         string = input('>>>')
    #         file.write(string + '\n')

    my_file = list(open('test.txt'))
    print(my_file)
    # my_file.close()
    print('{:}'.format(112223334))

def main():
    open_file()


if __name__ == '__main__':
    main()
