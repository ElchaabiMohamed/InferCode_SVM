def sousChaine(s,debut,longueur):
  res=""
  if (longueur+debut)>len(s):
    longueur=len(s)
  if (debut+len(s))>len(s):
    longueur=len(s)
  else:
    longueur=debut+longueur
  for i in range(debut,longueur):
    res=res+s[i]
  return res
