def suiteGeo(liste):
  ok=True
  i=0
  if len(liste)==0 and len(liste)==1:
    ok=True
  while i<len(liste)-2 and ok:
    q=liste[1]*liste[0]
    if liste[i]==0:
      ok=False
    elif liste[i+1]/liste[i]!=q:
      ok=False
    i=i+1
  return ok