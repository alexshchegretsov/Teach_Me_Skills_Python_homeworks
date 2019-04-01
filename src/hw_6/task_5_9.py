"""
Написать игру. Пользователь должен угадать число.
Сперва вводиться диапазон угадывания. После колличество попыток.
В случае правильного ответа - выводить You are the winner.
В случае неправильного давать игроку подсказку(больше или меньше искомое число).
Если за указанное количество попыток число не угадано - выводить: You are the loser и
правильное число.

"""
from random import randint as rd
from time import sleep

while True:
    first_num = int(input('Enter first number of range, from:\t'))
    last_num = int(input('Enter last number of range, to:\t'))
    attempts_amount = int(input('Enter attempts amount:\t'))
    desired_num = rd(first_num, last_num)
    print('Now try to guess the number!')
    sleep(2)

    while attempts_amount:
        user_attempt = int(input(f'Attempts left: {attempts_amount}\nEnter your number:\t'))

        if user_attempt == desired_num:
            print(f'You won, desired number is {desired_num}')
            break
        else:
            if user_attempt < desired_num:
                print(f'Desired number is greater than {user_attempt}')
            else:
                print(f'Desired number is less than {user_attempt}')
        attempts_amount -= 1
    else:
        print(f"You're loser, desired number is {desired_num}! :)")
        sleep(2)
    choice = input("If you want to quite game - enter 'q', if play - just press 'Enter': ")
    if choice.lower() != 'q':
        continue
    else:
        break