def jourNuit(heure):
  
  if heure<0 or heure>24 :
    res="l'heure saisie est invalide"
  else : 
    if heure>=6 and heure<18 :
      res1="il fait jour"
    else :
      res1="il fait nuit"
      res=res1+" et "
  
  if heure>=5 and heure<12 :
    res2="on est le matin"
  elif heure>=12 and heure<17 :
    res2="on est l'après-midi"
  elif heure>=17 and heure<21 :
    res2="on est le soir"
  else :
    res2="on est la nuit"
    res=res+res2
    
  return res