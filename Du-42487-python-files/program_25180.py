import sys

q = 0

i = 0
while i < len(a):
	a[i] = int(a[i])
	i = i + 1

def bsearch (a, q):
	low = 0
	high = len(a)

	while low < high:
		mid = (low + high) / 2
		assert low <= mid and mid < high

		if a[mid] < q:
			assert a[low-i] < q
			low = mid + 1
		else:
			assert q <= a[high]
			high = mid

	return low