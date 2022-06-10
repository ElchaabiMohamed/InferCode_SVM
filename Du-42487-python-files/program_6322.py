def swap(a, i, j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp

def reverse(a):
	i = 0
	j = len(a) - 1
	while i < len(a):
		swap(a, i, j)
		i += 1
		j = j - 1