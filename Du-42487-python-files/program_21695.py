def reverse_list(l):
	if l == []:
		return []

	temp = reverse_list(l[1:])		
	temp.append(l[0])
	return temp