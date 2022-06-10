import sys

my_dict = {'a': 4, 'b': 7, 'c': 10}

new_dict = []

for k, v in list(my_dict.items()):
    del my_dict[k]
    my_dict[v] = k
    new_dict.append(my_dict)

print(new_dict)
