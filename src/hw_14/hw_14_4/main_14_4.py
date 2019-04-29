from exceptions_14_4 import validation_operation, validation_numbers
from ui_func_14_4 import Menu


def main():
    while True:
        Menu().display_menu()
        choice = validation_operation()
        print(validation_numbers(choice))
        Menu().press_enter()


if __name__ == '__main__':
    main()
