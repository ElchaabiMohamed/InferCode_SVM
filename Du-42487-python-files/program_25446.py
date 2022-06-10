a = [1, 2, 3, 1, 2, 3]
def selection_sort(a):
	p = 0
	j = 1
	while j < len(a):
		if a[j] < a[p]:
			p = j	
		j = j + 1
	return a
