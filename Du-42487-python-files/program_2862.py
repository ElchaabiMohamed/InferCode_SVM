def maximum(lis,p=0):
	if lis == []:
		return p
	n=lis.pop()
	if n>p:
		p=n
	return minimum(lis,p)