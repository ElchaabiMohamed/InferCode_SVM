#!/usr/bin/env python3

def reverse_list(l):
    if not l or len(l) == 1:
        return l
    return [l[-1]] + reverse_list(l[:-1])
