def selectionsort(a):

	i=0
	while i<len(a):
		p=i
		j=i+1
		while j<len(a):
			if a[j] < a[p]:
				p=j
			j+=1
		a[i], a[p] = a[p], a[i]
		i+=1
	return a


print((selectionsort([4, 1, 3, 2])))
