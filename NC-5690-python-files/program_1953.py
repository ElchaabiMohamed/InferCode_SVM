def suiteGeo(liste):
  ok=True
  i=1
  if len(liste)==0 and len(liste)==1:
    ok=True
  while i<len(liste)-1 and ok:
    if liste[i]==0:
      ok=False
    q=liste[1]/liste[0]
    if liste[i+1]/liste[i]!=q:
      ok=False
    i=i+1
  return ok