def nbOccurrencesLettre(lettre,mot):
	res=0
	for l in mot:
		if l==lettre:
			res+=1
	return res