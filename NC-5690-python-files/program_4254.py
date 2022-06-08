def listeSymetrique(l):
  ok=True
  i=0
  while i<len(l) and ok:
    if l[i]!=l[-i-1]:
      ok=False
    else:
      ok=True
    i+=1
  return ok
