def reverse(n):
	a=[]
	i = 0
	j = len(n)-1
	while i < len(n)/2:
		tmp = a[i]
		a[i] = a[j]
		a[j] = tmp
		i = i + 1

	print(a)