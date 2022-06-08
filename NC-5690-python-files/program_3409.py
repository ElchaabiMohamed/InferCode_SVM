def suiteGeo(liste):
  ok=True
  i=0
  if liste[0]==0:
    ok=False
  q=liste[0]*liste[1]
  while i<len(liste)-1 and ok:
    if liste[i]!=0:
      if liste[i+1]/liste[i]!=q:
        ok=False
    i=i+1
  return ok