def sommeNPremiersEntiersPairs(n):
	res=0
	if n<0:
		res=0
	for i in range(1,n+1):
		if i%2==0:
			res=res+i
	return res