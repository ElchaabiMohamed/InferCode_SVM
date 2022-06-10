def reverse(a, i, j):
	a=[]

	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

	return a