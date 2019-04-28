import sys


def quit_program() -> None:
    sys.exit(0)


def addition(x: str, y: str) -> int:
    return eval(f'{x}+{y}')


def substraction(x: str, y: str) -> int:
    return eval(f'{x}-{y}')


def multiply(x: str, y: str) -> int:
    return eval(f'{x}*{y}')


def division(x: str, y: str) -> int:
    return eval(f'{x}/{y}')


def press_enter_to_continue() -> None:
    input('press ENTER to continue >>>')
