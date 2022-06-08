def listeSymetrique(l):
  ok=True
  i=0
  j=len(l)-1
  while i<j and ok:
    if l[i]!=l[j]:
      ok=False
    i+=1
    j-=1
  return ok