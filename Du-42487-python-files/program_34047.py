def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	i = 0
	j = a[len(a) - 1]
	while i < len(a):
		swap(a,i,j)
		i = i + 1
		j = j - 1