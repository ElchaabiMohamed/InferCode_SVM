import sys

def swap_keys_values(d):
    print(d)
    new_dict = {}
    i = 0
    while i < len(d):
        new_dict[d[i]] = d[0]
        i += 1
    return new_dict