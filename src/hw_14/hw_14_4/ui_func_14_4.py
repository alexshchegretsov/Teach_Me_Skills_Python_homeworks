import sys


class Menu:

    def display_menu(self):
        print('-' * 55)
        print('\t\t\t\t    CALCULATE')
        print('enter the appropriate number to perform the operation')
        print('-' * 55)
        print("""
                    1. Add
                    2. Sub
                    3. Mult
                    4. Div


types: int, float, complex""")
        print('-' * 55)
        print('\t\t\t\tFor EXIT enter 0')
        print('-' * 55)

    @staticmethod
    def press_enter():
        input('press ENTER to continue >>>')

    @staticmethod
    def quit_program():
        sys.exit(0)
