def binary_search(a,q):
	low = 0
	high = len(a)
	i = 0
	while i < len(a) and a[low] <= q:
		mid = (high + low) / 2
		if a[mid] < q:
			low = mid + 1
		else:
			low = mid - 1
	return low