def indiceOccurrence(n,x,l):
  i=0
  cpt=0
  trouve=False
  res=None
  while i<len(l) and not trouve:
    if x==l[i]:
      cpt+=1  
    if n==cpt:
      trouve=True    
    i+=1
    res=i-1
  return res