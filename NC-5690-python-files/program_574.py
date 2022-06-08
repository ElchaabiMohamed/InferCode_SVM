def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for i in range(len(liste)-1):
    c=a*liste[i]+b
    c.append(c)
    if c==liste:
      res=True
  return res