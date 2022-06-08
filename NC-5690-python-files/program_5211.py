def indiceOccurrence(n,x,l):
  cpt=0
  i=0
  res=0
  while i<len(l):
    if l[i] == x and cpt<n:
      cpt+=1
      res=i
    i+=1   
  if cpt < n:
    return None
  else: return res
  return None