def suiteAriGeo(liste):
  res=True
  if len(liste)>2:
    if (liste[1]-liste[0])==0:
      q=0
      r=0
    else:
    	q=(liste[2]-liste[1])/(liste[1]-liste[0])
    	r=liste[1]-q*liste[0]
    res=verifSuiteAriGeo(liste,q,r)
  return res

def verifSuiteAriGeo(liste,a,b):
  ok=True
  n=1
  while n<len(liste) and ok:
    if liste[n]!=liste[n-1]*a+b:
      ok=False
    n+=1
  return ok