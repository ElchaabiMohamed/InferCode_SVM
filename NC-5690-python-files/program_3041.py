def listeSymetrique(l):
  ok=True
  i=0
  while i<len(l)/2 and ok:
    if l[i]!=l[-1-i]:
      ok=False
    i=i+1
  return ok