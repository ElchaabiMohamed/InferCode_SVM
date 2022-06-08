def verifSuiteAriGeo(liste,a,b):
  c=[]
  for elem in liste:
    c+=a*elem+b
    if c==elem:
      res=True
  return res