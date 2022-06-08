def indiceOccurrence(n,x,l):
  i=0
  cpt=0
  trouve=False
  while i<len(l) and trouve==False:
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
      trouve=True
    i=i+1
  if trouve:
    res=i-1
  else:
    res=None
  return res