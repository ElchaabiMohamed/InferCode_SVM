import sys

def swap_keys_values(d):
    new_dict = {}
    for k, v in list(d.items()):
        new_dict[v] = k
    return new_dict

print((swap_keys_values(dicti)))