def premiereOccurrenceLettre(lettre,mot):
	res = None
	for l in range(len(mot)):
		if lettre == mot[l]:
			if res == None:
				res = l
	return res