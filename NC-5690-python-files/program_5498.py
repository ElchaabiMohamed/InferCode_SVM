def jourNuit(heure):
  if 5<=heure<6:
    res='on est le matin et il fait nuit'
  elif 6<=heure<12:
    res='on est le matin et il fait jour'
  elif 12<=heure<17:
    res="on est l'après-midi et il fait jour"
  elif 17<=heure<18:
    res='on est le soir et il fait jour'
  elif 18<=heure<21:
    res='on est le soir et il fait nuit'
  elif 0<=heure<5 or 21<=heure<=24:
    res='on est la nuit et il fait nuit'
  else:
    res="l'heure saisie est invalide"
  return res
            