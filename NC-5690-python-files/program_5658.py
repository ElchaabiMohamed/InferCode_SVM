def verifSuiteAriGeo(liste,a,b):
  c=[]
  for elem in liste:
    c+=a*liste[elem]+b
    if c==liste[elem]:
      res=True
  return res