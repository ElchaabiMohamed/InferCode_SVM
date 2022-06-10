def reverse_list(li):
	newli = []
	if len(li) == 1:
		return li
	x = li.pop()
	newli.append(x)
	s = reverse_list(li)
	for i in s:
		newli.append(i)
	return newli