def sommeNbPairs(liste):
  if liste==[] :
    res=0
  else:
    res=0
    for elem in liste:
      if elem%2==0 :
        res=res+elem
  return res