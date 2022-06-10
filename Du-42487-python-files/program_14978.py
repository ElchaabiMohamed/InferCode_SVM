#!/usr/bin/env python
a = []
s = input()
while 0 < len(a):
	a.append(int(a))
	s = input() 

i = 0
while i < len(a):
	a[i] = int(a[i])
	i = i + 1

def bsearch(a,q):
	low = 0
	high = len(a)

	while low < high: 
		mid = (low + high) / 2
		assert low <= mid and mid < high

		if a [mid] < q:
			low = mid + 1
			assert a[low-1] < q
		else:
			high = mid
			assert q <= a[high]

	return low

p = bsearch(a,q)
