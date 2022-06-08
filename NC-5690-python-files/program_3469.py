def jourNuit(heure):
  if heure<0 or heure>24:
    heure="l'heure saisie est invalide"
  if 6<=heure<=18:
    if 5<=heure<=12:
      heure="on est le matin et il fait jour"
    if 12<=heure<=17:
      heure="on est l'après-midi et il fait jour"
    if 17<=heure<=18:
      heure="on est le soir et il fait jour"
  if 1<=heure<=5 or 19<=heure<=24:
    if 1<=heure<=4:
      heure="on est la nuit et il fait nuit"
    if 21<=heure<=24:
      heure="on est la nuit et il fait nuit"
    if 19<=heure<=20:
      heure="on est le soir et il fait nuit"
  return heure