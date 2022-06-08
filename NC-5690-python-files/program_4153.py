def verifSuiteAriGeo(liste,a,b):
  res=True
  i=1
  while i<len(liste):
    if liste[i]!=a*liste[i-1]+b:
      res=False
    i+=1
  return res