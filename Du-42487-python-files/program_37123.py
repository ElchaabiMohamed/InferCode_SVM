def reverse_list(l):
	if not l:
		return l
	else:
		temp = reverse_list(l[1:])
		temp.append(l[0])
		return temp
		
