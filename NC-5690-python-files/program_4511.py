def indiceOccurrence(n,x,l):
  trouve=False
  i=0
  cpt=0
  res=None
  while i<len(l) and trouve==False:
    if l[i]==x:
      cpt=cpt+1
    if n==cpt:
      trouve=True
    i=i+1
  if trouve==True:
    res=(i-1)
  return res