def swap(a, x, y):
	tmp = a[x]
	a[x] = a[y]
	a[y] = tmp
	return a
def reverse(a):
	i = 0
	while i < len(a) / 2:
		swap(a, i, len(a) - i -1)
		i += 1
	return a
