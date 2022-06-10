def selectionsort(a):
	i = 0
	while (i <len(a)):
		j = i +1
		p = i	
		while (j < len(a)):
			if (a[p] >= a[j]):
				p = j
			j +=1
		tmp = a[i]
		a[i] = a[p]
		a[p] = tmp
		i +=1