import sys

def swap_keys_values(dictionary):
    new_dict = {}
    for k, v in list(dictionary.items()):
        new_dict[v] = k

