i = 0

q = 0

a = []

while i < len(a):
	a[i] = int(a[i])
	i = i + 1

def bsearch(a, q):
	low = 0
	high = len(a)

	while low < high:
		mid = (low + high) / 2
		assert low <= mid and mid < high

		if a[mid] < q:
			assert a[mid + 1-1] < q
			low = mid + 1
		else:
			high = mid

	return low