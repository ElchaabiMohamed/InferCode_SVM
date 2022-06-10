def quicksort(a, start, end):
	if end - start < 1:
		return
	i = k = start
	while i <= end:
		if a[i] <= a[end]:
			a[i], a[k] = a[k], a[i]
			k = k + 1
		i = i + 1

	quicksort(a, start, k - 2)
	quicksort(a, k, end)
