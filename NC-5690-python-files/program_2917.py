def jourNuit(heure):
  Error="l'heure saisie est invalide"
  Time="on est"
  if heure<=0 or heure>=24:
    res=Error
  elif heure>=5 and heure<12:
    res=Time+' le matin'
    if heure>=6 and heure<=18:
      res=res+' et il fait jour'
    else:
      res=res+' et il fait nuit'
  elif heure>=12 and heure<17:
    res=Time+" l'après-midi et il fait jour"
  elif heure>=17 and heure<21:
    res=Time+' le soir'
    if heure>=6 and heure<=18:
      res=res+' et il fait jour'
    else:
      res=res+' et il fait nuit'
  else:
    res=Time+' la nuit et il fait nuit'
  return res
    
  
    