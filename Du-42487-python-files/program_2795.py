import sys

def swap_unique_keys_values(dictionary):
    new_dict = {}
    for k, v in list(dictionary.items()):
        if v in new_dict:
            del new_dict[v]
        else:
            new_dict[v] = k
    return new_dict
