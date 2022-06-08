def jourNuit(heure):
  if heure>24 or heure<0:
    afficher="l'heure saisie est invalide"
  else:
    if 0<=heure<=5 or 5<=heure<=12:
      afficher="on est le matin et il fait nuit"
    if 21<=heure<=24 and 0<=heure<=5:
      afficher="on est la nuit et il fait nuit"
    if 12<=heure<=17 or 6<=heure<=18:
      afficher="on est l'apres-midi et il fait jour"
    if 17<=heure<=21 or 6<=heure<=18:
      afficher="on est le soir et il fait jour"
     
  return afficher