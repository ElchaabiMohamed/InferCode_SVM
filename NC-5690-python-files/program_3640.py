def suiteGeo(liste):
  ok=True
  i=0
  while i<len(liste)-1 and ok:
    q=liste[1]*liste[0]
    if liste[i+1]/liste[i]!=q:
      ok=False
    i=i+1
  return ok