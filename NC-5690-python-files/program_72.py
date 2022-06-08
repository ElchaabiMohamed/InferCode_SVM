def jourNuit(heure):
  if heure > 24 or heure < 0 :
    res = ("l'heure saisie est invalide")
  elif heure >= 6 and heure <= 18 :
    if heure >= 5 and heure <= 12 :
      res = ("on est le matin et il fait jour")
    elif heure > 12 and heure < 17 :
      res = ("on est l'après-midi et il fait jour")
    else :
      res = ("on est le soir et il fait jour")
  else :
    if heure >= 5 and heure < 12 :
      res = ("on est le matin et il fait nuit")
    elif heure > 12 and heure < 17 :
      res = ("on est l'après-midi et il fait nuit")
    elif heure > 17 and heure < 21 :
      res = ("on est le soir et il fait nuit")
    else :
      res = ("on est la nuit et il fait nuit")
  return res