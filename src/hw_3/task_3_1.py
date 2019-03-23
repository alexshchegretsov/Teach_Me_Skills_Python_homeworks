number = int(input('Enter any number:\t'))
while True:
    if number % 1000 == 0:
        print('millennium')
        break
    else:
        number = int(input('Enter another number:\t'))
