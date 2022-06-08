def compare(chaine1,chaine2):
  i=0
  while res==0 and i<chaine1 and i<chaine2:
    if chaine1[i]<chaine2[i]:
      res=-1
    elif chaine1[i]>chaine2[i]:
      res=1
    else:
      res=0
  return res