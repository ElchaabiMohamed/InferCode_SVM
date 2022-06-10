import sys

def swap_keys_values(d):
    new_d = {v : k for k, v in list(d.items())}
    return new_d


