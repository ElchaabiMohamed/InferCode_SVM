def listeSymetrique(l):
  i=0
  ok=True
  while i<len(l) and ok:
    if l[i]!=l[-(i+1)]:
      ok=False
    i=i+1
  return ok