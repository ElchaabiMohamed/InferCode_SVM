#!/usr/bin/env python

def swap(a,i,j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp

def reverse(a):
    i = 0
    n = len(a) - 1
    while n < len(a)/2:
        if a[j] < a[n]:
            swap(a,i,j)
        n = n + 1
