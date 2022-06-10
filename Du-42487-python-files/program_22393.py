#!/usr/bin/env python

import sys

def bsearch(a,q):
	low = 0
	high = len(a)

	while low < high:
		middle = (low + high) /2
		if a[mid] < q:
			low = mid
			assert low == 0 or a[low-1] < q
		else:
			high = mid
			assert high == len(a) or q <= a[high]
		

