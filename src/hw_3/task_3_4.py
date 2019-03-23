string = input('Enter any string:\t')
central_char = string[len(string) // 2]
print(central_char)
if central_char is string[0]:
    string_slice = string[1:-1]
    print(string_slice)
