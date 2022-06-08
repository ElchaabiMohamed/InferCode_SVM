def ecart(liste):
	if len(liste) == 0:
		res = None
	else:
		ma = liste[0]
		mi = liste[0]
		for i in range(len(liste)):
			if liste[i] > ma and liste[i] > mi:
				ma = liste[i]
			else:
				mi = liste[i]
	res = ma - mi
	return res