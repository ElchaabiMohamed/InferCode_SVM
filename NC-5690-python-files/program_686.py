def indiceOccurrence(n,x,l):
  cpt=0
  trouve=False
  i=0
  res=None
  while i<len(l) and trouve:
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
      trouve=True
      res=i
    i=i+1
  return res

      
    