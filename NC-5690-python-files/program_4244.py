def listeSymetrique(l):
  i=0
  j=-1
  ok=True
  while i<(len(l))/2 and ok:
    if l[i]!=l[j]:
      ok=False
    i=i+1
    j=j-1
  return ok