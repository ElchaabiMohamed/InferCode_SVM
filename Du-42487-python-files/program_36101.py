def reverse_list(l):
	new_list = []
	i = 0
	while len(l) > i:
		new_list.append(l.pop())
		i += 1
		
	return new_list	


