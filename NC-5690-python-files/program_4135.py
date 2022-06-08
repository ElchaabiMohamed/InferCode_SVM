def indiceOccurrence(n,x,l):
  cpt=0
  trouve=0
  i=0  
  while i<len(l) and trouve==False:
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
      trouve=True
  i=i+1    
#post-traitement
  if trouve!=n:
    i=-1
  return i    