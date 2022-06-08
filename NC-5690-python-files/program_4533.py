def compare(chaine1,chaine2):
  res=0
  i=0
  while i<len(chaine1) and i<len(chaine2):
    if chaine[i]<chaine2[i]:
      res=-1
    else:
      if chaine[i]>chaine2[i]:
        res=1
      else:
        res=0
    i=i+1
  return res