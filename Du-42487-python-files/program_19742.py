#a = []
def reverse(a):
	a = []
	i = 0
	while i < len(a):
		tmp = a[i]
		a[i] = a[len(a) - i - 1]
		a[len(a) - i - 1] = a[i]
	return a

