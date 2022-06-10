def minimum(l):
	if len(l) == 1:
		return l[0]
	i = 0
	if l[i] > l[i+1]:
		i = i + 1
		l = l[i]
	else:
		l.pop(i + 1)
	return minimum(l)
