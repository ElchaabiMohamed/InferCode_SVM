def bsearch(a, q):
	low = 0
	high = len(a)
	while low < high:
		mid = low + (high - low) / 2
		if a[mid] < q:
			low = mid+1
		elif a[mid] >= q:
			high = mid

	return low