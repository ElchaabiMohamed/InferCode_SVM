#!/usr/bin/env python3

def maximum(l):
    biggest = l[0]
    for e in l:
        if e < biggest:
            biggest = e
    return biggest
