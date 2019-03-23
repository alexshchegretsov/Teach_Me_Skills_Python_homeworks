"""
Ввести предложение состоящее из двух слов.
Поменять местами слова, добавить восклицательный знак в начало и конец,
вывести итоговое предложение на экран.

"""
sent = input('Enter two words:\t')
sent_list = sent.split(' ')
swap_sent = '!{0} {1}!'.format(sent_list[1], sent_list[0])
print(swap_sent)
