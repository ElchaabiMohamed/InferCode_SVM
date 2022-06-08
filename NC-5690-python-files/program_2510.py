def compare(chaine1,chaine2):
  i=0
  res=0
  while res==0 and i<len(chaine1) and i<len(chaine2):
    if chaine1[i]<chaine2[i]:
      res=-1
    elif chaine1[i]>chaine2[i]:
      res=1
    i=i+1
  if res==0 and len(chaine1)>len(chaine2):
    res=1
  elif res==0 and len(chaine1)<len(chaine2):
    res=-1
  return res