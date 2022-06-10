def reverse_list(l):
	if l == []:
		return []

	temp = reverse_list(l[1:])		#l list's every elements[1:0] except 1st one(l[0])
	temp.append(l[0])
	return temp