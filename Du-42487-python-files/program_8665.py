#!/usr/bin/env python3

def swap_keys_values(d):
    dic = {}
    for key in d:
        value = d[key]
        dic[value] = key 
    return dic