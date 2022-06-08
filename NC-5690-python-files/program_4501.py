def ecart(liste):
	if len(liste)==0:
		res=0
	else:
		ma=max(liste)
		mi=min(liste)
		res=ma-mi
	return res

    