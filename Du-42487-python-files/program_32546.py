def bsearch(a, q):
	low = 0
	high = len(a)
	
	while low < high:
		mid = (low + high) / 2
		if a[mid] < q:
			low = mid + 1  #self note: adding + 1 cause integer division
		else:              #rounds down whenever a remainder is present
			high = mid

	return low