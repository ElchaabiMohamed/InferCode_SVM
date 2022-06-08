def indiceOccurrence(n,x,l):
  cpt=0
  trouve=False
  i=0
  while i<len(l) and trouve==False:
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