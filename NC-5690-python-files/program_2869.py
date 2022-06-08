def sousChaine(s,debut,longueur):
  fin= debut+longueur
  if fin>len(s):
    fin=debut+longueur
  for i in range(debut,fin):
      res=res+s[i]
  return res