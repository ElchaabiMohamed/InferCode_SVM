def compare(chaine1,chaine2):
  res=0
  i=0
  while i<len(chaine1) and res==0:
    if chaine1[i]<chaine[2]:
      res=-1
    if chaine1[i]>chaine[2]:
      res=1
    else:
      res=0
    i=i+1
  return res
