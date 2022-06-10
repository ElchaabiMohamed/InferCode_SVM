#!/usr/bin/env python3

def swap_unique_keys_values(d):
    d2 = {}
    d3 = {}
    sortd = sorted(list(d.items()), reverse = True)
    return sortd