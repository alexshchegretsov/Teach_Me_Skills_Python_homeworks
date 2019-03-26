string = 'adjlllxlllflfl86953][aadfh(dg#zz'
i = 0
letters = [0] * 26
length = len(letters)

for char in string.lower():
    if 'a' <= char <= 'z':
        char_number = ord(char) - 97
        letters[char_number] += 1

max_char_repeat = max(letters)
while i < length:
    if letters[i] > 0:
        char = chr(i + 97)
        char_repeat = char * letters[i]
        char_repeat_length = len(char_repeat)
        if char_repeat_length == max_char_repeat:
            print(char)
            break
    i += 1
