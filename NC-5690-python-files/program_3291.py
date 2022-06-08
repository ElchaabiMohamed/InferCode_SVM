def SommeNbPairs(liste):
  res=0
  for x in liste:
    if x%2==0:
      res=res+x
  return res