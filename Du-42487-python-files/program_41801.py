#!/usr/bin/env python3

def swap_keys_values(d):
    new_d = {}
    for k,v in zip(d):
        new_d[v] = k
    return new_d