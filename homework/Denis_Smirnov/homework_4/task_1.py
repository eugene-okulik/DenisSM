my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {
        'key_1': '1',
        'key_2': '2',
        'key_3': '3',
        'key_4': '4',
        'key_5': '5'
    },
    'set': {1, 2, 3, 4, 5}
}

tuple_last_element = my_dict['tuple'][-1]
print(tuple_last_element)


my_dict['list'].append(6)
print(my_dict['list'])
del my_dict['list'][1]
print(my_dict['list'])


my_dict['dict'][('i am tuple',)] = '6'
print(my_dict['dict'])
del my_dict['dict']['key_2']
print(my_dict['dict'])


my_dict['set'].add(6)
print(my_dict['set'])
my_dict['set'].remove(4)
print(my_dict['set'])


print(my_dict)
