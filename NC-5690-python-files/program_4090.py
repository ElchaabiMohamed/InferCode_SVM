def verifSuiteAriGeo(liste,a,b):
  res=True
  n=1
  while n<len(liste) and res:
    if liste[n]!=liste[n-1]*a+b:
      res=False
    n+=1
  return res