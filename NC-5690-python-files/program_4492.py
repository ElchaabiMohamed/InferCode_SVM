def sommeNbPairs(liste):
  if liste==0:
    res=0
  else:
    for n in (liste):
      if n%2==0:
        res=res+n
    return res