def reverse_list(l):
	if len(q) != 0:
		temp = q.pop(0)
		reverse(q)
		q.append(temp)
	return q
