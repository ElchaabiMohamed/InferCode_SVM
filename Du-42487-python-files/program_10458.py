def reverse_list(a):
	i = 0
	while i < len(a)/2:
		tmp = a[i]
		a[i] = a[len(a)-1-i]
		a[len(a)-1-i] = tmp
		i += 1
	return a