def rendezVous(debut1,fin1,debut2,fin2):
	res=False
	if debut2<=debut1:
		if fin2>=debut1:
			res=True
	if debut2<=fin1:
		if fin2>=fin1:
			res=True
	if debut1==None or debut2==None or fin1==None or fin2==None:
		res=False
	return res