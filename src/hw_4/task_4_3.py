"""
 Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа
(пример {‘key’: ‘value’} -> {‘key3’: ‘value’})

"""
dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_dict = {}
length = len(dictionary)
while length > 0:
    recover_pair = dictionary.popitem()
    list_recover_pair = list(recover_pair)
    add_value = str(len(list_recover_pair[0]))
    list_recover_pair[0] += add_value
    new_dict.update([list_recover_pair])
    length -= 1
print(new_dict)
