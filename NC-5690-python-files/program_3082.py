def jourNuit(heure):
  res=[]
  if heure<0:
    res="l'heure saisie est invalide"
  if heure>24:
    res="l'heure saisie est invalide"
  if 6<=heure<=18:
    if 5<heure<=12:
      res="on est le matin et il fait jour"
    elif 12<=heure<=17:
      res="on est l'après-midi et il fait jour"
    elif 17<=heure<=18:
      res="on est le soir et il fait jour"
  if 1<=heure<=5 or 19<=heure<=24:
    if 1<=heure<=4:
      res="on est la nuit et il fait nuit"
    elif 21<=heure<=24:
      res="on est la nuit et il fait nuit"
    elif 19<=heure<=20:
      res="on est le soir et il fait nuit"
  return res