def reverse(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

	return a