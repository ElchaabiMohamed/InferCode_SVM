def listeSymetrique(l):
  i=0
  n=0
  while i<len(l/2) and n==0:
    if l[i]==l[len(l)-i-1]:
      i=i+1
      n=0
    else:
      n=1
  if n==0:
    res=True
  else:
    res=False
  return res
    