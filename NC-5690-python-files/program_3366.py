def verifSuiteAriGeo(liste,a,b):
  for elem in liste:
    c=a*liste[elem]+b
    if c==elem:
      res=True
  return res