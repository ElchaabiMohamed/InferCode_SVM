def indiceOccurrence(n,x,l):
  trouve=False
  i=0
  cpt=0
  while i<len(l) and not trouve:
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
     trouve=True
    i=i+1
  if l==[]:
    res=None
  return res