def maximum(li):
	if len(li) == 1:
		return li[0]
	big = li.pop(0)
	v = maximum(li)
	if big < v:
		big = v
	return big