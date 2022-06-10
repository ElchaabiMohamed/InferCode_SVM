def union(x,y):
	answer = []
	check = {}
	
	i = 0
	while i < len(x):
		if not (x[i] in check):
		   answer.append(x[i])
		   check[x[i]] = True
		i = i + 1

	j = 0
	while j < len(y):
		if not (y[j] in check):
			answer.append(y[j])
			check[y[j]] = True
		j = j + 1

	return answer

def intersection(x,y):
	check = {}

	i = 0
	while i < len(x):
		if x[i] in y and not (x[i] in check):
			check[x[i]] = True
		i = i + 1

	return check
