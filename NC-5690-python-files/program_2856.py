def compare(chaine1,chaine2):
  res=0
  i=0
  if len(chaine1)<len(chaine2):
    while i<len(chaine1) and res==0:
      if chaine1[i]<chaine2[i]:
        res=-1
      if chaine1[i]>chaine2[i]:
        res=1
      if chaine1[i]==chaine2[i]:
        res=0
      i=i+1
  else:
    while i<len(chaine2) and res==0:
      if chaine1[i]<chaine2[i]:
        res=-1
      if chaine1[i]>chaine2[i]:
        res=1
      if chaine1[i]==chaine2[i]:
        res=0
      i=i+1
    
  return res
