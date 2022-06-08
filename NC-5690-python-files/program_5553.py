def indiceOccurrence(n,x,l): #A faire plus tard ca m a soule
  cpt=0
  i=0
  while i<len(l) and cpt<n:
    if l[i] == x :
      cpt+=1
    i+=1   
  if cpt != n:
    return None
  else: return i-1
