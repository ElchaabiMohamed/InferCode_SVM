#!/usr/bin/env python

def swap(a , i, j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp

def find_position_of_smallest(a,i):
	n = 1
	i = 1
	while i < len(a):
		if a[i] < a[n]:
			n = i 
		n = n + 1
	return 
