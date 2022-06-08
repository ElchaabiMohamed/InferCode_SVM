def listeSymetrique(l):
  res=True
  i=0
  j=-1
  while i<len(l) and j<len(l):
    if l[i]==l[j]:
      i=i+1
      j=j-1
    else:
      res=False
      i=i+1
      j=j+1
  return res