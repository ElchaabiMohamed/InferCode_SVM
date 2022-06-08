def sommeNPremiersEntiers(n):
	res=0
	if n<0:
		res=0
	for i in range(1,n+1):
		res=res+i
	return res