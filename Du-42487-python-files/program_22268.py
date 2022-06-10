#!/usr/bin/env python 

import sys 

q = 6

a = [1,2,3,4,5,6,7,8,9]


def bsearch(a,q):
	low = 0
	high = len(a)

	while low < high: 
		mid = (low + high) / 2
		assert low <= mid and mid < high 

		if a[mid] < q:
			low = mid + 1
		else: 
			high = mid

	return low 