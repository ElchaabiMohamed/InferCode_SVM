#!usr/bin/env python3

def reverse_list(l):
    return l if len(l) < 2 else reverse_list(l[1:]) + [l[0]]
