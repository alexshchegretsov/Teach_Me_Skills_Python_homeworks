from typing import Tuple


def validation_operation() -> str:
    while True:
        choice = input("Choose operation >>>")
        if choice.isdigit() and 0 <= int(choice) <= 4:
            return choice
        else:
            print(f"There is no operation {choice}")


def validation(choice: str) -> Tuple[int, int]:
    while True:
        if choice in ["1", "2", "3"]:
            try:
                num_1 = int(input('first operand >>>'))
                num_2 = int(input('second operand >>>'))
                return num_1, num_2
            except (ValueError, TypeError) as er:
                print(f'Error - {er}')
        else:
            try:
                num_1 = int(input('first operand >>>'))
                num_2 = int(input('second operand >>>'))
                if not num_2:
                    print('ZeroDivisionError')
                else:
                    return num_1, num_2
            except (ValueError, TypeError) as er:
                print(f'Error - {er}')
