def verifSuiteAriGeo(liste,a,b):
  ok=True
  n=1
  while n<len(liste) and ok:
    if liste[n]!=liste[n-1]*a+b:
      ok=False
    n+=1
  return ok
def suiteGeo(liste):
  res=True
  if len(liste)>1:
    q=0
  else:
    q=liste[1]/liste[0]
  res=verifSuiteAriGeo(liste,q,0)
  return res