# part 1
my_dict = {'Краснодар' : 38, 'Локомотив' : 34, 'Спартак' : 31, 'Динамо' : 31}
print (my_dict)
print(my_dict['Спартак'])
print(my_dict.get('ЦСКА'))
my_dict.update({'Рубин' : 22,
                'Ростов' : 20})
x = my_dict.pop('Локомотив')
print (x)
print (my_dict)

# part 2
my_set = {10, 11, 12, 11, 12, 13, 10, True, 'текст1', (14, 15)}
my_set = set(my_set)
print (my_set)
my_set.add(9)
my_set.add('текст2')
my_set.discard(True)
print (my_set)