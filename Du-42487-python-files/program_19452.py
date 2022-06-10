def swap(a, x ,y):
	tmp = a[x]
	a[x] = a[y]
	a[y] = tmp
	return a
def selection_sort(a):
	k = 0
	while k < len(a):
		j = k + 1
		p = k
		tmp = 0
		while j < len(a):
			if a[j] < a[p]:
				p = j
			j += 1
		swap(a, k, p)
		k += 1
	
