def suiteAriGeo(liste):
  i=0
  while i<len(liste)-1:
    a=liste[i]-liste[i-1]
    b=liste[i]-liste[i-1]
    if liste[i+1]==liste[i]+b:
      a=1
    if liste[0]!=0:
      if liste[i+1]==liste[1]/liste[0]:
        b=0
    i=i+1
  ok=True
  i=0
  if len(liste)==0 or len(liste)==1:
    ok=True
  while i<len(liste)-1 and ok:
    if liste[i+1]!=a*liste[i]+b:
      ok=False
    i=i+1
  return ok