#!/usr/bin/env python
def selection_sort(a):
	i = 0
	while i < len(a):
		j = i + 1
		min_ind = i
		while j < len(a):
			if a[j] < a[min_ind]:
				min_ind = j
			j += 1

		tmp = a[i]
		a[i] = a[min_ind]
		a[min_ind] = tmp

		i += 1
