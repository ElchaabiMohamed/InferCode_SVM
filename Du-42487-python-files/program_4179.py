def union(x,y):
	answer = []
	check = {}
	
	i = 0
	while i < len(x):
		if not (x[i] in check):
		   answer.append(x[i])
		   check[x[i]] = True
		elif not (y[i] in check):
			answer.append(y[i])
			check[y[i]] = True
		i = i + 1

	