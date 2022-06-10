def selectionsort(n):
	i = 0
	while i < len(n):

		p = i
		j = i + 1
		while j < len(n):
			if n[j] < n[i]:
				p = j
			j += 1

		tmp = n[p]
		n[p] = n [i]
		n[i] = tmp
		i =+ 1