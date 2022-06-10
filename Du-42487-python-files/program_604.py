import sys

def swap_keys_values(d):
    dict_ = sys.argv[1]
    new_dict = {}
    for k, v in list(dict_.items()):
        new_dict[v] = k

