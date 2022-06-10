def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	
def reverse(a):
	swap(a, i, j)
	
	i = 0
	while i < len(a):
		x = a[len(a) - i - 1]
