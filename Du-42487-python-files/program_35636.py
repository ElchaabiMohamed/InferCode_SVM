#!/usr/bin/env python

def bsearch(a,q):
    low = 0
    high = len(a)-1
    while low != high:
        if high < low:
            return -1
        mid = (low + high) / 2
        if a[mid] < q:
            low = mid + 1
        else:
            return mid
