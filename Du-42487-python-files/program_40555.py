def union(x,y):
	answer = []
	check = {}
	
	i = 0
	while i < len(x):
		if not (x[i] in check):
		   answer.append(x[i])
		   check.append(x[i])

		i = i + 1

	j = 0
	while i < len(y):
		if not (y[j] in check):
			answer.append(y[j])
			check.append(y[j])
		j = j + 1

	return answer