#!/usr/bin/env python3

def minimum(a):
    if len(a) == 1:
        return a[0]
    if a[0] < minimum(a[1:]):
        return a[0]
    else:
        return minimum(a[1:])