#!/usr/bin/env python

def swap (a,i,j):
    tmp = a [i]
    a [i] = a [j]
    a [j] = tmp

def reverse (a):
    i = 0
    while i < len (a):
        tmp = a [i]
        a [i] = a [-i]
        a [-i] = tmp
