#!/usr/bin/env python

def swap(a,i,j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = a[j]

def reverse(a):
    i = 0
    while i < len(a):
        print(a[len(a) - i - 1])
        i = i + 1

        