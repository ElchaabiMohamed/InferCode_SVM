def jourNuit(heure):
  if heure<0 or heure>24:
    res="l'heure saisie est invalide"
  else:#l'heure est valide
    if heure<5 or heure>=21:
      res="On est la nuit"
    elif heure<12:
      res="On est le matin"
    elif heure <17:
      res="On est l'après-midi"
    else:
      res="On est le soir"
    if heure<6 or heure>=18:
      res=res+"et il fait nuit"
    else:
      res=res+"et il fait jour"
  return res