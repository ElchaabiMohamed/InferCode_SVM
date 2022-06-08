def sousChaine(s,debut,longueur):
  res=""
  if debut+longueur>len(s):
    fin=len(s)
  else:
    fin=debut+longueur
  for i in range(debut,debut+longueur):
    s=res+s[i]
  return res  