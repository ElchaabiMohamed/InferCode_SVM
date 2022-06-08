def suiteAriGeo(liste):
  i=0
  while i<len(liste)-1:
    a=liste[0]
    b=liste[0]
    if liste[i]==0 and liste[i+1]==0:
      a=1
      b=0
    if liste[i+1]==liste[i]+(liste[1]-liste[0]):
      b=liste[1]-liste[0]
    if liste[0]!=0:                        
      if liste[i+1]==liste[i]*liste[1]/liste[0]:
        a=liste[1]/liste[0]
        b=0
    if liste[i+1]==liste[i]*(liste[1]-liste[0])+(liste[i]-(liste[i-1]*(liste[1]-liste[0]))):
      a=liste[1]-liste[0]
      b=liste[i]-(liste[i-1]*a)
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