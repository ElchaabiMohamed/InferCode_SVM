def indiceOccurrence(n,x,l):
  cpt=0
  i=0
  trouve=False
  res=None
  while i<len(l) and not trouve :
    if l[i]==x :
      cpt+=1
      if cpt==n :
        trouve=True
        res=i
    i+=1
  
  return res