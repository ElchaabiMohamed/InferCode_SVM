def sousChaine(s,debut,longueur):
  res=""
  if (longueur+debut)>len(s):
    longueur=len(s)
  else:
    longeur=debut+longueur
  for i in range(debut,longueur):
    res=res+s[i]
  return res