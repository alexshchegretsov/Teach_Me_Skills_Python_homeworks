my_file = open('hw_10.txt')
strings = my_file.readlines()
my_file.close()
print(strings)
string_1 = 'str10'
new_string = [x.strip('\n') for x in strings if '\n' in x]
new_string_2 = [*map(lambda s: s.strip('\n'), strings)]
new_string_str_1 = [*map(lambda s: s.strip('\n'), strings)]
# remove_n = lambda x: x != '\n', strings
new_string_3 = [*filter(lambda x: x != '\n', 'wert\n')]

# for i in range(len(strings)):
#     if '\n' in strings[i]:
#         strings[i] = strings[i].strip('\n')

print(new_string)
