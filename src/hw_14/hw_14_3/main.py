from exceptions import validation_operation, validation_numbers
from ui_func import menu
from func import press_enter_to_continue


def main():
    while True:
        menu()
        choice = validation_operation()
        print(validation_numbers(choice))
        press_enter_to_continue()


if __name__ == '__main__':
    main()
