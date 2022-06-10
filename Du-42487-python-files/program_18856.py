import sys

def swap_keys_values(d):
    new_dict = {}
    i = 0
    while i < len(d):
        new_dict[d[0]] = d[1]
        i += 1
    return new_dict