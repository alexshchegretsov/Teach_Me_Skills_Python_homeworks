from exceptions_14_4 import validation_operation, validation
from ui_func_14_4 import Menu
from classes_14_4 import Math


def main():
    while True:
        Menu.display_menu()
        choice = validation_operation()
        if choice == "0":
            Menu.quit_program()
        num_1, num_2 = validation(choice)
        units = {
            "1": Math(num_1, num_2).addition,
            "2": Math(num_1, num_2).substraction,
            "3": Math(num_1, num_2).multiply,
            "4": Math(num_1, num_2).division,
        }
        print(units[choice]())
        Menu.press_enter()


if __name__ == '__main__':
    main()
