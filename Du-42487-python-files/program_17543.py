#!/usr/bin/env python

def bsearch(a,q):
    low = 0
    high = len(a)-1
    while low != high:
        mid = (low + high) / 2
        if a[mid] < q:
            low = low + 1
        else:
            return low
