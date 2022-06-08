def ecart(liste):
	if len(liste)==1:
		res=1
	if len(liste)==0:
		res=0
	ma=max(liste)
	mi=min(liste)
	res=ma-mi
	return res

    