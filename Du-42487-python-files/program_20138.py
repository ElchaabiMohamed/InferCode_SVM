#!/usr/bin/env python3

def swap_unique_keys_values(dict):
    return {v: k for k, v in list(dict.items()) if dict.values.count(v) == 1}

if __name__ == '__main__':
    print((swap_keys_values({'a': 1, 'b': 2})))
