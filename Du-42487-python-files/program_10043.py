a = [1, 2, 3, 1, 2, 3]
def selection_sort(a):
	p = 0
	j = 1
	while j < len(a):
		if a[j] < a[p]:
			p = j
			a[j] = tmp
			a[p] = a[j]
			tmp = a[p]
		j = j + 1

		a[j] = tmp
		a[p] = a[j]
		tmp = a[p]

	return a
