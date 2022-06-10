#!usr/bin/env python3

def maximum(l):
    if len(l) == 1:
        return l[0]
    else:
        n, m = l[0], maximum(l[1:])
        return n if n > m else m
