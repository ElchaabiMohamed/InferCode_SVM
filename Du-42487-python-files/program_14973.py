import sys

my_dict = {'a': 4, 'b': 7, 'c': 10}


def swap_keys_values(s):
    for k, v in list(my_dict.items()):
        del my_dict[k]
        my_dict[v] = k

    print(my_dict)
