def suiteAri(liste):
  res=True
  if len(liste)>1:
    r=liste[1]-liste[0]
    res=verifSuiteAriGeo(liste,1,r)
  return res

def verifSuiteAriGeo(liste,a,b):
  ok=True
  n=1
  while n<len(liste) and ok:
    if liste[n]!=liste[n-1]*a+b:
      ok=False
    n+=1
  return ok