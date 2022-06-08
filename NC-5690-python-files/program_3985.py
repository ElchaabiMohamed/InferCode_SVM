def indiceOccurrence(n,x,l):
  i=0
  cpt=0
  trouve=False
  while i<len(l) and not trouve:
    if l[i]==x:
      cpt+=1
    if cpt==n:
      trouve=True
    i+=1
  if trouve:
    res=i-1
  else:
    res=None
  return res