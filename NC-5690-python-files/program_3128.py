def jourNuit(heure):
  if heure<0 or heure >24:
    res="l'heure saisie est invalide"
  else:
    if heure<5:
      res="on est la nuit"
    elif heure<12:
      res="on est le matin" 
    elif heure<17:
      res="on est l'apres midi"
    elif heure<21:
      res="on est la soir"
    if heure<6 or heure>18:
      res=res+" et il fait nuit"
    else:
      res=res+" et il fait jour"
  return res