def moyenne(liste):
	if len(liste) == 0:
		res= None
	else:
		nb = 0
		res = 0
		for elem in liste:
			res = res + elem
			nb+=1
		moy = res / nb
	return moy