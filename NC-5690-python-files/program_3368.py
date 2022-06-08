def listeSymetrique(l):
  ok=True
  i=0
  while i<len(l) and ok:
    if l[i]!=l[-1-i]:
      ok=False
    i+=1
  return ok