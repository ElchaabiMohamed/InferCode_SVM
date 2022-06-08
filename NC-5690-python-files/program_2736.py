def indiceOccurrence(n,x,l):
  cpt=0
  trouve=False
  i=0
  res=None
  while i<len(l) and trouve==False:
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
      trouve=True
    i=i+1
    if trouve==True:
      res=i-1
    else:
      res=None
  return res

      
    