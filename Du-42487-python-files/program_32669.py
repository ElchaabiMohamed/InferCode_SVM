def partition(a, start, end):
	j = q = start

	while j < end:
		if a[j] < a[end]:
			a[j], a[q] = a[q], a[j]
			q += 1
		j += 1

	a[end], a[q] = a[q], a[end]
	return q


def quicksort(a, start, end):
	
	if end<=start:
		return

	q = partition(a, start, end)
	quicksort(a, start, q-1)
	quicksort(a, q+1, end)



