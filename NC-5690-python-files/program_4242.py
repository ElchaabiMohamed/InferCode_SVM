def suiteAriGeo(liste):
  i=0
  while i<len(liste) and len(liste)!=0:
    a=liste[1]-liste[0]
    b=liste[1]-liste[0]  
  ok=True
  i=0
  if len(liste)==0 or len(liste)==1:
    ok=True
  while i<len(liste) and ok:
    if liste[i+1]!=a*liste[i]+b:
      ok=False
    i=i+1
  return ok