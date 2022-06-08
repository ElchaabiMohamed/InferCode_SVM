def premiereOccurrenceLettre(lettre,mot):
	res=0
	for l in range(len(mot)):
		if lettre==mot[l]:
			res=l
        
	return res