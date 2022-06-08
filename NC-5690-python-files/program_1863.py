def indiceOccurrence(n,x,l):
  res=None
  i=0
  cpt=0
  while i<len(l) and cpt!=n:
      if l[i]==x:
        cpt+=1
      i+=1
  if cpt==n:
    res=i-1
  return res
    