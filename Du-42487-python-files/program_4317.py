def minimum(li):
	if len(li) == 1:
		return li[0]
	small = li.pop(0)
	v = minimum(li)
	if v < small:
		small = v
	return small