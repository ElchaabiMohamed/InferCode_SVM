#!/usr/bin/env python3

def reverse_list(l):
    if not l:
        return []
    return reverse_list[0].append(reverse_list(l[1:]))
