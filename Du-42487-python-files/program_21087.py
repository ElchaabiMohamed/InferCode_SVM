import sys

def swap_unique_keys_values(d):
    return{v : k for (k, v) in list(d.items())}
