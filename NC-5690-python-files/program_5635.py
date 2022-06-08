def premiereOccurrenceLettre(lettre,mot):
	res=None
	for i in range(len(mot)):
		if lettre==mot[i]:
			if res==None:
				res=i       
	return res