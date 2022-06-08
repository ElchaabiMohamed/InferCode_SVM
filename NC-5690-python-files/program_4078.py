def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for elem in liste:
    c=a*elem+b
    res=True
  if c==[]:
    res=True
  return res