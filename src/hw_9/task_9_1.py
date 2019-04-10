"""
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
где i это порядковый номер строки в списке. Использовать генератор списков.
"""

some_string = 'every day is exactly the same'
new_list = [f'{i} - {string}' for i, string in enumerate(some_string.split())]

