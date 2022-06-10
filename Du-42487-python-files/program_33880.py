#!/usr/bin/env python

def selection_sort(a):
	i = 0
	while i < len(a):
		p = i
		j = i + 1
		while j < len(a):
			if a[j] < a[p]:
				p = j
			i = i + 1

		tmp = a[i]
		a[i] = a[p]
		a[p] = tmp
		i = i + 1
	return a