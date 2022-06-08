def sousChaine(s,debut,longueur):
  res=0
  fin=debut+longueur
  if longueur>len(s):
    fin=len(s)
  for i in range(debut,fin):
    res=res+s[i]
  return res