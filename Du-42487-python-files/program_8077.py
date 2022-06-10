#!/usr/bin/env python
a = []

def selection_sort(a):
	p = i
	j = i + 1
	while j<len(a):
		if a[j]<a[p]:
			p = j
		j = j + 1
	return p

i = 0
while i<len(a):
	p = selection_sort(a,i)

	tmp = a[i]
	a[i] = a[p]
	a[p] = tmp

	i = i + 1