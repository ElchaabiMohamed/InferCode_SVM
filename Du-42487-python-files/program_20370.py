#!/usr/bin/env python

def bsearch(a, q):
	low = 0
	high = len(a)
	assert low == 0 or a[low-1] < q
	assert high == len(a) or q <= a[high]
	while low < high:
		mid = (low + high) / 2
	
	if a[mid] < q:
		low = mid + 1
	else:
		high = mid

	return low