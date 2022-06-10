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

def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp	

i = 0
while i<len(a):
	p = selection_sort(a,i)
	swap(a,i,p)
	i = i + 1