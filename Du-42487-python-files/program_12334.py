def minimum(lis,p=0):
	if lis == []:
		return p
	n=pop(lis)
	if n>p:
		p=n
	return minimum(lis)