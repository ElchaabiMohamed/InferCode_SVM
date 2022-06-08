def listeSymetrique(l):
  if l==[]:
    ok=True
  else:
    ok=True
    i=0
    while i<len(l) and ok:
      if l[i]!=l[-i-1]:
        ok=False
      i+=1
  return ok