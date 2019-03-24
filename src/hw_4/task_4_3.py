"""
 Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа
(пример {‘key’: ‘value’} -> {‘key3’: ‘value’})

"""
dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
length = len(dictionary)
current_keys_list = list(dictionary.keys())
i = 0
while i < length:
    current_key_name = current_keys_list[i]
    add_item = str(len(current_key_name))
    new_key_name = f'{current_key_name}{add_item}'
    dictionary[new_key_name] = dictionary[current_key_name]
    del dictionary[current_key_name]
    i += 1
print(dictionary)






