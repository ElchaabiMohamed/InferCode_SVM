def jourNuit(heure):
    res = "l'heure saisie est invalide"

    if heure <= 24:
        if heure >= 5 and heure < 12:
            res = "on est le matin "
        elif heure >= 12 and heure < 17:
      	    res = "on est l'après-midi "
        elif heure >= 17 and heure <= 21:
            res = "on est le nuit "
        else:
            res = "on sais pas c'est pas dis "
        if heure >= 6 and heure <= 18:
            res += "et il fait jour"
        else:
            res += "et il fait nuit"
    return res
      