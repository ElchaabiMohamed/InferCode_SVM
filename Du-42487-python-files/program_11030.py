def selection_sort(a):
	for i in range(len(a)):
		mini = min(a[i:])
		min_index = a[i:].index(mini)
		a[i+min_index] = a[i]
		a[i] = mini
		return a