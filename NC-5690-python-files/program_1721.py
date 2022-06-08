def compare(chaine1,chaine2):
  res=0
  i=0
  while i<len(chaine1) and i<len(chaine2) and res==0:
    if chaine1[i]<chaine2[i]:
      res=-1
    elif chaine1[i]==chaine2[i]:
      res=0
    else:
      res=1
    i=i+1
  #traiter le cas où les deux chaines sont identiques mais l'une est plus longue que l'autre
  if res==0:
    if len(chaine1)>len(chaine2):
      res=1
    elif len(chaine1)<len(chaine2):
      res=-1
  return res
   