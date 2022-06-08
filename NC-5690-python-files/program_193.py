def listeSymetrique(l):
  i=0
  j=-1
  res=True
  while i<(len(l))/2 and j>(-len(l))/2 and res==True:
    if l[i]!=l[j]:
      res=False
    i=i+1
    j=j-1
  return res