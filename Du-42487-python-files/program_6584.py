a = []
def reverse(a):
	i = 0
	while i < len(a):
		tmp = a[i]
		a[i] = a[len(a) - i]
		a[len(a) - i] = a[i]
	return a

