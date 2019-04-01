"""
В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы.
"""
string = 'what are you doing'
string = ' '.join(string.split(' ')[::-1])
print(string)

