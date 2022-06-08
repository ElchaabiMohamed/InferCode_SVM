def indiceOccurrence(n,x,l):
  cpt=0
  i=0
  res=None
  while i<len(l) and cpt<n:
    if l[i]==x:
      cpt=cpt+1
    i=i+1
  if cpt==n:
    res=i
  return res