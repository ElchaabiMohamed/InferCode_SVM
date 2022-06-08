def indiceOccurence(n,x,l):
  trouve=False
  cpt=0
  i=0
  res=None
  while i<len(l) and not trouve :
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
      res=i
    i=i+1
  return res