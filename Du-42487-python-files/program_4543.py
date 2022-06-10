def swap(a,i,j):
	temp = a[j]
	a[j] = a[i]
	a[i] = temp
def reverse(a):
	i = 0
	j = len(a) - 1
	while i < (len(a) / 2):
		temp = a[j]
		a[j] = a[i]
		a[i] = temp
		i = i + 1
		j = j - 1