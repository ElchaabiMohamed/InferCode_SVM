#!/usr/bin/env python3

def reverse_list(a):
    if len(a) == 1:
        return a[0]
    return [a[-1]] + reverse_list(a[::-1])