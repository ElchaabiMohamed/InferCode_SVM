def ecart(liste):
	if len(liste)==0:
		res=None
	else:
		res=max(liste)-min(liste)
	return res

    