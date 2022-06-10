def maximum(l):
	if len(l) == 1:
		return l[0]
	
	i = 0
	j = 1
	while i < len(l) - 1 and l[i] > l[j]:
		i +=1
		j +=1
	
	l.pop(i)
	maximum(l)
	return l[0]