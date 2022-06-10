#!usr/bin/env python

import sys

def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def smallest_element(a, i):
		p = i 
		j = i + 1
		while j < len(a):
			if a[p] < a[j]:
				p = j
			j = j + 1

		return p

def selection_sort(a):
	i = 0
	while i < len(a):
		smallest_element(a,i)
		swap(a, i, j)
		i = i + 1