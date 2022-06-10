def maximum(l):
	#print(l)
	if len(l) == 1:
		return l[0]
	else:
		m = maximum(l[1:])
		if m > l[0]:
			#print('ping')
			return m
		else:
			#print('pong')
			return l[0]