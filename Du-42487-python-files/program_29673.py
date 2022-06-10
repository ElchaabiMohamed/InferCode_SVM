def maximum(lst):
	if len(lst) == 1:
		return lst[0]
		
	if lst[0] > lst[1]:
		lst.remove(lst[q])
		
	else:
		lst.remove(lst[0])
		
	return maximum(lst)
		
