def bissextile(annee):
	if annee%4==0:
		res=True 
	elif annee%100!=0:
		res=False
	elif annee%400==0:
		res=True
	return res