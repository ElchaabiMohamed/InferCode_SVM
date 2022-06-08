def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for elem in liste:
    c=a*elem+b
    if c==liste[elem]+1:
      res=True
  if c==[]:
    res=True
  return res