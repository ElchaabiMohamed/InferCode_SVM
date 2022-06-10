#!/usr/bin/env python

def swap(a,i,p):
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

def selection_sort(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            p = j
        j = j + 1

    swap(a,i,p)
    i = i + 1
