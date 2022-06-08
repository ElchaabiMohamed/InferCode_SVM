def jourNuit(heure):
  
  if heure<0 or heure>24 :
    res="l'heure saisie est invalide"
  else : 
    if heure>=6 and heure<18 :
      res="et il fait jour"
    else :
      res="et il fait nuit"
  
  if heure>=5 and heure<12 :
    res="on est le matin"+res
  elif heure>=12 and heure<17 :
    res="on est l'après-midi"+res
  elif heure>=17 and heure<21 :
    res="on est le soir"+res
  else :
    res="on est la nuit"+res
    
  return res