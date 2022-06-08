def indiceOccurrence(n,x,l):
  res=None
  trouve=False
  cpt=0
  i=0
  while i<len(l) and trouve==False:
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
      trouve=True
      res=i
    i=i+1
  return res