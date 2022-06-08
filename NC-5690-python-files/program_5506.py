def rendezVous(debut1,fin1,debut2,fin2):
	res=False
	if fin2<=debut1<=debut2:
		res=True
	if fin2<=fin1<=debut2:
		res=True
	return res