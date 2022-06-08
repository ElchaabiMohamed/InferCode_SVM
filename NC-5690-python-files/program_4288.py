def sommeNbPairs(liste):
  res=0
  for nbrs in liste:
    if nbrs%2==0:
      res=res+nbrs
  return res