string = 'adjlllxlllflfl86953][aadfh(dg#zz'
i = 0
letters = [0] * 26
length = len(letters)

for char in string.lower():
    if char >= 'a' and char <= 'z':
        char_number = ord(char) - 97
        letters[char_number] += 1
print(letters)


while i < length:
    item = letters[i]
    if item > 1:
        current_char = chr(item + 97)
        string_repeats = current_char * letters[item]
        print(string_repeats)
        if len(string_repeats) == max(letters):
            print(item)
            print(string_repeats)
            break
    i += 1

# for char in range(26):
#     string_repeats = chr(char + 97) * letters[char]
#     if len(string_repeats) == max(letters):
#         print(chr(char + 97))