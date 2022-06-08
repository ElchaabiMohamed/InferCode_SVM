def sousChaine(s,debut,longueur):
  fin=0
  res=""
  if (longueur+debut)>len(s):
    fin=len(s)
  for i in range(debut,fin):
    res=res+s[i]
  return res

