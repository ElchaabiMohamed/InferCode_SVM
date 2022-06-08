def suiteGeo(liste):
  ok=True
  i=0
  if len(liste)==0 or len(liste)==1:
    ok=True
  while i<len(liste)-1 and ok:
    if liste[0]==0:
      ok=False
    if liste[i]!=0:
      q=liste[1]/liste[0]
    if liste[i]!=0:
      if liste[i+1]/liste[i]!=q:
        ok=False
    if liste[i] and liste[i+1]==0:
      ok=True
    if liste[i]==0 and liste[i+1]==0:
      ok=True
    i=i+1
  return ok
