def sommeNbPairs(liste):
  res=0
  if liste==[]:
    res=res
  else:
    for n in liste:
      if n%2==0:
        res=res+n
  return res
        
        
      