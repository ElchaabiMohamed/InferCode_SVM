def ecart(liste):
	if len(liste)==0:
		res=None
	else:
		ma=max(liste)
		mi=min(liste)
		res=max(liste)-min(liste)
	return res

    