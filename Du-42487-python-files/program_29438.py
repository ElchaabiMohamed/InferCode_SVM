def reverse_list(li):
	
	newli = []
	if len(li) == 1 or len(li) == 0:
		return li
	x = li.pop(0)
	newli = reverse_list(li)
	newli.append(x)
	return newli
	