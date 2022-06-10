def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	
def reverse(a):
	swap(a, i, j)
	a[len(a) - i - 1]
