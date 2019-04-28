from func import (
    addition,
    substraction,
    multiply,
    division,
    quit_program,
)


def validation_operation() -> str:
    while True:
        choice = input("Choose operation >>>")
        if choice.isdigit() and 0 <= int(choice) <= 4:
            return choice
        else:
            print(f"There is no operation {choice}")


def validation_numbers(choice: str) -> int:
    while True:
        if choice == "0":
            quit_program()
        num_1 = input('first operand >>>')
        num_2 = input('second operand >>>')

        if choice == "1":
            try:
                return addition(num_1, num_2)
            except (NameError, SyntaxError) as er:
                print(f'Error - {er}')

        elif choice == "2":
            try:
                return substraction(num_1, num_2)
            except (NameError, SyntaxError) as er:
                print(f'Error - {er}')

        elif choice == "3":
            try:
                return multiply(num_1, num_2)
            except (NameError, SyntaxError) as er:
                print(f'Error - {er}')

        elif choice == "4":
            try:
                return division(num_1, num_2)
            except (NameError, ZeroDivisionError, SyntaxError) as er:
                print(f'Error - {er}')
