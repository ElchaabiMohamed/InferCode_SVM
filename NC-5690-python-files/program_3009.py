def jourNuit(heure):
	if heure<0 or heure>24:
		n="l'heure saisie est invalide"
	if 6<=heure<=18:
		n='et il fait jour'
		if 6<=heure<=12:
			n='on est le matin '+n
		if 13<=heure<=17:
			n="on est l'après-midi "+n
		else:
			n='on est le soir '+n
	if heure<=5 or heure>=19:
		n='et il fait nuit'
		if heure<=5:
			n='on est la nuit '+n
		if heure==5:
			n='on est le matin '+n
		if 19<=heure<=21:
			n='on est le soir '+n
		else:
			n='on est la nuit '+n
	
		
