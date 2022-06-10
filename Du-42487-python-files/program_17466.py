def selection_sort(a):
	for i in range(len(a)):
		least = i
		for k in range(i+1, len(a)):
			if a[k] < a[least]:
				least = k
		tmp = a[i]
		a[i] = a[k]
		a[k] = tmp