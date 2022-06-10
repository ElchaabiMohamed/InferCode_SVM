def bsearch(a, q):
	low = 0
	high = len(a)

	while low < high:
		mid = (low + high) / 2
		if a[mid] < q:
			low = mid
			assert low == 0 or a[low - 1] < q
		else:
			high = mid
			assert high == len(a) or q <= a[high]
		return high - mid