def bissextile(annee):
	if annee%4==0 and annee%100!=0:
		if annee%400==0:
			res=True
		else:
			res=False
	else:
		res=False
	return res