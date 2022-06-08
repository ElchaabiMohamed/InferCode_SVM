def suiteGeo(liste):
  ok=True
  i=0
  while i<len(liste)-1 and ok:
    if liste[i]==0:
      ok=False
    if liste[i]!=0:
      q=liste[0]*liste[1]
    if liste[i]!=0:
      if liste[i+1]/liste[i]!=q and q!=0:
        ok=False
    i=i+1
  return ok
    