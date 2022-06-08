def listeSymetrique(l):
  i=0
  ok=True
  while i<len(l)//2 and ok:
    if l[i]!=l[-i-1]:
      ok=False
    i=i+1
  return ok
