def suiteGeo(liste):
  ok=True
  i=1
  while i<len(liste) and ok:
    q=liste[2]/liste[1]
    if liste[i]==0:
      ok=False
    if liste[i]/liste[i-1]!=q:
      ok=False
    i=i+1
  return ok
    