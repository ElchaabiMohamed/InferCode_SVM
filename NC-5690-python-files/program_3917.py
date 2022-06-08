def indiceOccurrence(n,x,l):
  cpt=0
  i=0
  while i<len(l) and i<n:
    if l[i]==x:
      cpt+=1
    i+=1
  if i!=n:
    res=None
  else:
    res=i
  return res