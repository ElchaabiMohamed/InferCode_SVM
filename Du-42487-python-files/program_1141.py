def minimum(lis,p=100000000000000000000000000000000000000000000):
	if lis == []:
		return p
	n=lis.pop()
	if n<p:
		p=n
	return minimum(lis,p)