def indiceOccurence(n,x,l):
  res=None
  cpt=0 
  trouve=False 
  i=0
  while i<len(l) and not trouve:
    if l[i]==x:
      cpt+=1
    if cpt==n:
      trouve=True
      res=i
    i+=1
  return res
      