#!usr/bin/env python

import sys

def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def selection_sort(a):
	i = 0
	while i < len(a):
		p = i 
		j = i + 1
		while j < len(a):
			if a[p] < a[j]:
				j = p
			j = j + 1
		i = i + 1

	swap(a,i,p)