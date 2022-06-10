def minimum(l):
	a = l[len(l)-1]
	if len(a)==1:
		return l[0]
	if a >= minimum(l):
		return minimum([j for j in l[:-1]])
	