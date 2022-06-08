def elemArisuiteAri(liste):
  ok=True
  cpt=u0
  i=0
  if len(liste)==0:
    ok=True
  while i<len(liste) and ok:
    cpt=cpt+r
    if liste[i+1]!=cpt:
      ok=False
    i=i+1
  return ok
    
    