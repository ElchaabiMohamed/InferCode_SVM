def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	return a

i = 0
j = len(a) - 1
def reverse(a):
	while i < len(a)/2:
		swap(a, i, j)
		i = i + 1
		j = j - 1
	return a
