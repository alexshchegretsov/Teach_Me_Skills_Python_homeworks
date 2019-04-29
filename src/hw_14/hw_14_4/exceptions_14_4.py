from classes_14_4 import Math
from ui_func_14_4 import Menu


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
            Menu().quit_program()

        num_1 = input('first operand >>>')
        num_2 = input('second operand >>>')

        if choice == "1":
            try:
                return Math(num_1, num_2).addition()
            except (NameError, SyntaxError, TypeError) as er:
                print(f'Error - {er}')

        elif choice == "2":
            try:
                return Math(num_1, num_2).substraction()
            except (NameError, SyntaxError, TypeError) as er:
                print(f'Error - {er}')

        elif choice == "3":
            try:
                return Math(num_1, num_2).multiply()
            except (NameError, SyntaxError, TypeError) as er:
                print(f'Error - {er}')

        elif choice == "4":
            try:
                return Math(num_1, num_2).division()
            except (NameError, ZeroDivisionError, SyntaxError, TypeError) as er:
                print(f'Error - {er}')
