#!/usr/bin/env python

def swap(a , i, j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp

def find_position_of_smallest(a,i):
	n = 0
	i = 0
	while i < len(a):
		if a[i] > a[n]:
			n = i 
		i = i + 1
	return n 
