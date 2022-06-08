def sommeNbPairs(liste):
  res=0
  if len(liste)==0:
    res=0
  for elem in liste:
    if elem%2==0:
      res=res+elem
  return res