def swap(a,i,j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp
	return
def reverse(a):
	return swap(a,2,3)
