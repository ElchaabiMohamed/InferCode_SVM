def suiteGeo(liste):
  ok=True
  i=0
  if len(liste)==0 or len(liste)==1:
    ok=True
    q=liste[i+1]/liste[i]
  while i<len(liste)-1 and ok:
    if liste[i]!=0:
      if liste[i+1]/liste[i]!=q:
        ok=False
    i=i+1
  return ok

