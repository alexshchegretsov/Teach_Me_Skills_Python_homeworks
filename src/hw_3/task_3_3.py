string = input('Enter some string:\t')
if len(string) > 10:
    print(f'{string}!!!')
elif len(string) <= 10:
    second_char = string[1]
    print(f"{second_char} - it's the second char")
