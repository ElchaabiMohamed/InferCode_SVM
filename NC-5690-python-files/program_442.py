def jourNuit(heure):
  0<=heure<=24
  if 6<=heure<=18 :
    temps='il fait jour'
  else :
    temps='il fait nuit'
  if 0<=heure<=5 and 21<=heure<=24 :
    soleil='on est la nuit'
  if 5<=heure<=12 :
    soleil='on est le matin'
  if 12<=heure<=17 :
    soleil="on est l'après-midi"
  if 17<=heure<=21 :
    soleil="on est le soir"
  heure= temps
  return heure