def jourNuit(heure):
  if heure > 24 or heure < 0 :
    res = "l'heure saisie est invalide"
  else :
    if heure < 5 :
      res = "on est la nuit "
    elif heure < 12 :
      res = "on est le matin "
    elif heure < 17 :
      res = "on est l'après-midi "
    else :
      res = "on est le soir "
    if heure >= 6 and heure < 18 :
      res = res + "et il fait jour"
    else :
      res = res + "et il fait nuit"
  return res