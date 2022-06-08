def indiceOccurrence(n,x,l):
  trouve=False
  i=0
  cpt=0
  while i<len(liste) and not trouve:
    if liste[i]==x:
      i=i+1
      cpt=cpt+1
    if cpt==n:
     trouve=True
  res=i
  return res