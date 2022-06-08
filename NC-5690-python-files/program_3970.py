def indiceOccurrence(n,x,l):
  res=None
  i=0
  cpt=0
  while i<len(l) and cpt<n:
    if l[i]==x:
      cpt+=1
    if cpt==n:
      res=i
    i+=1
  return res