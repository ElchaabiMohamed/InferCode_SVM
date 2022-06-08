def suiteAriGeo(liste):
  i=0
  while i<len(liste)-1:
    a=liste[1]-liste[0]
    b=liste[1]-liste[0]
    if liste[i+1]==liste[i]*a:
        b=0
        a=liste[1]/liste[0]
    if liste[i+1]==liste[i]+b:
      a=1
      b=liste[1]-liste[0]
    i=i+1
  i=0
  ok=True
  if len(liste)==0 or len(liste)==1:
    ok=True
  while i<len(liste)-1 and ok:
    if liste[i+1]!=a*liste[i]+b:
      ok=False
    i=i+1
  return ok