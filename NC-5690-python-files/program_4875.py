def sousChaine(s,debut,longueur):
  res=''
  if debut+longueur > len(s):
    longueur=len(s)-debut
  else:
    for i in range (debut,debut+longueur):
      res=res+(debut+longueur)[i]
  return res