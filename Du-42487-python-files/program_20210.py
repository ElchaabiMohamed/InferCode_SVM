def reverse_list(l, i = 0):
	if i == len(l) // 2:
		return l
	tmp = l[i]
	l[i] = l[len(l) - 1 - i]
	l[len(l) - 1 - i] = tmp
	i += 1
	
	return reverse_list(l, i)
