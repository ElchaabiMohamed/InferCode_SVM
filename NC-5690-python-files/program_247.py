def jourNuit(heure):
  h=heure[0]
  if 0>h or h>24:
    res="l'heure saisi est invalide"
  else:
    if h>=5 and h<=12:
      res="on est le matin"
    else:
      if h>=12 and h<=17:
        res="on est l'après-midi"
      else:
        if h>=17 and h<=21:
          res="on est la nuit"
  if h>=6 and h<=18:
    res=res+" il fait jour"
  else:
    res=res+" il fait nuit"
    
    return res