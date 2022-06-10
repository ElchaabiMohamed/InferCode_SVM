def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	i = 0
	j = len(a) - 1
	while i < j:
		swap(a, i, j)
		i += 1
		j -= 1