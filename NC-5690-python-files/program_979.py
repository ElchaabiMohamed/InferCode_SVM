def indiceOccurrence(n,x,l):
  i=0
  cpt=0
  trouve=False
  if l==[]:
    res=None
  else:
    while i<len(l) and not trouve:
      if x==l[i]:
        cpt+=1  
      if n==cpt:
        trouve=True    
      i+=1
      res=i-1
    if n>cpt:
      res=None
    elif cpt==0:
      res=None
  return res