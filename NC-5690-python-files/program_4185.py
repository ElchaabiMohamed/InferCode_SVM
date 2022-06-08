def sousChaine(s,debut,longueur):
  res=""
  if debut+longueur>len(s):
    fin=len(s)
  for i in range(debut,debut+longueur):
    res=res+s[i]
  else:
    fin=debut+longueur
  return res
    