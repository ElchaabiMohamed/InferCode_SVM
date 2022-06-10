#!/usr/bin/env Python

# Your function definition goes here.

def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a): 
	i = 0 
	j = len(a) - 1 
	while i < (len(a) / 2):
		swap(a, a[i], a[j])
		i = i + 1 
		j = len(a) -i -1
	return a