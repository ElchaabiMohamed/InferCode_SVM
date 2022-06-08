def listeSymetrique(l):
  ok=True
  i=0
  while i<len(l) and ok:
    if l[i]!=l[-i]:
      ok=False
    i+=1

  return res