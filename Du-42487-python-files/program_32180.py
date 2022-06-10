#!/usr/bin/env python3

def swap_keys_values(d):
    tmp = ""
    for key in d:
        key = key.split()
        tmp = key[0]
        key[0] = key[1]
        key[1] = tmp
    return d