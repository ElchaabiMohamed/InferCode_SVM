#!/usr/bin/env python3

def minimum(l):
    smallest = l[0]
    for e in l:
        if e < smallest:
            smallest = e
    return smallest
