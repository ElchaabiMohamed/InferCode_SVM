def suiteGeo(liste):
  i=0
  ok=True
  while i<len(liste)-1 and ok:
    if liste[i]!=0:
      q=liste[i]/liste[0]
      if liste[i+1]/liste[i]!=q:
        ok=True
    i=i+1
  return ok