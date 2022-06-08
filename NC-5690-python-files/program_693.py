def jourNuit(heure):
  res=''
  if 6<=heure<=18 and 5<=heure<=12:
    res="on est le matin et il fait jour"
  if 6<=heure<=18 and 12<heure<17:
    res="on est l'apres-midi et il fait jour"
  if 17<heure<=18 and 6<=heure<=18:
    res="on est le soir et il fait jour"
  if 18<=heure<=5 and 17<=heure<=5:
    res="on est la nuit et il fait nuit"
  return res