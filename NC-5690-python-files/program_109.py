def bissextile(annee):
	if annee%4==0 or annee%400==0:		
		res=True
	elif annee%100==0:
		res=False
	return res