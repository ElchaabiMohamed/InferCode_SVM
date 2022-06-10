#!/usr/bin/env python3

def swap_keys_values(dict):
    return {v: k for k, v in list(dict.items())}

if __name__ == '__main__':
    print((swap_keys_values({'a': 1, 'b': 2})))
