def suiteAri(liste):
  ok=True
  if len(liste)==0:
    ok=True
def elemAri(n,u0,r):
  i=0
  while i<n and ok:
    cpt=cpt+r
    if liste[i+1]!=cpt:
      ok=False
    i=i+1
  return ok
    
    