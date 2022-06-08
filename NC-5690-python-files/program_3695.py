def compare(chaine1,chaine2):
  i=0
  res=0
  while i<len(chaine1) and i<len(chaine2) and res==0:
    if chain1[i]<chain2:
      res=-1
    if chain1[i]>chain2:
      res=1
  i=i+1
  return res

