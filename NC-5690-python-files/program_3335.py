def indiceOccurrence(n,x,l):
  ok=true
  i=0
  cpt=0
  while i<len(l) and ok:
    if l[i]==x:
      #instructions
      cpt=cpt+1
    if cpt==n:
      ok=False
    i=i+1
  if cpt!=n:
    i=None
  return i