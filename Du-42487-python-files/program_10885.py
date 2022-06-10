def maximum(l):
	max = -1*(sum(l))
	for i in l:
		if i > max:
			max = i
	return max