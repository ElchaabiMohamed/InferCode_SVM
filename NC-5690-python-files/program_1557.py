def indiceOccurrence(n,x,l):
  res=""
  cpt=0
  trouve=False
  i=0
  while i<len(l) and trouve==False:
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
      trouve=True
    i=i+1
  if cpt==False:
    res=None
  else:
    res=i

  return res