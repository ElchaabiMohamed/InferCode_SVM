def sommeNbPairs(liste):
  if liste==0:
    res=0
  else:
    for n in (liste):
      if liste[n]%2==0:
        res=res+liste[n]
    return res