def sousChaine(s,debut,longueur,fin):
  res=''
  if debut+longueur>len(s):
    fin=len(s)
  else:
    fin=debut+longueur
  for i in range(debut,Fin):
    res=res+s[i]
  return res