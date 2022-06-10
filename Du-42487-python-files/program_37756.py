#!/usr/bin/env python

import sys

def bsearch(a,q):
	low = 0
	high = len(a)

	while low < high:
		middle = (low + high) /2
		if a[middle] < q:
			low = middle + 1
			assert low == 0 or a[low-1] < q
		else:
			high = middle
			assert high == len(a) or q <= a[high]
		
		return low

