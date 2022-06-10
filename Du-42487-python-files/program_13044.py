
def reverse_list(l):

	if l == []:
		return l

	tmp = reverse_list(l[1:])
	tmp.append(l[0])

	return tmp
