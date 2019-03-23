user_input = input('Enter password:\t')
list_input = list(user_input)
if len(list_input) >= 10:
    for i in list_input:
        if i.isdigit():
            for x in list_input:
                if x.islower():
                    for y in list_input:
                        if y.isupper():
                            print('Safe')
else:
    print('wrong')


def checkio(string) -> bool:
    list_str = list(string)
    if len(list_str) >= 10:
        for i in list_str:
            if i.isdigit():
                for x in list_str:
                    if x.isupper():
                        for y in list_str:
                            if y.islower():
                                return True
    else:
        return False
