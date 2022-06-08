def indiceOccurrence(n,x,l):
  cpt=0
  i=0
  trouve=False
  res=0
  while i<len(l) and not trouve :
    if l[i]==x :
      cpt+=1
      if cpt==n :
        trouve=True
        res=i
    i+=1
  
  if (cpt<n) or (x not in l) :
    res=None

  return res