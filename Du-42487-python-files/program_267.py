
def bsearch(a, q):
	low = 0
	high = len(a)

	while low < high:
		mid = (low + high) / 2

		if a[mid] < q:
			low = mid + 1

		else:
			high = mid

	return low


def index_of(a, q):
	p = bsearch(a, q)

	if p < len(a) and a[p] == q:
		return p

	else:
		return 0

	