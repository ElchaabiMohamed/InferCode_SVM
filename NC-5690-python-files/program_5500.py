def quatrePlus100(liste):
	res=[]
	i=0
	cpt=0
	while i<len(liste) and cpt!=4:
		if liste[i]>100:
			res=res+[liste[i]]
			cpt=cpt+1
		i=i+1
	return res