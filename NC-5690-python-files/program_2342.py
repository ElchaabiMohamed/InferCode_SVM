def sousChaine(s,debut,longueur):
  res=''
  if debut+longueur>len(s):
    res=debut+longueur
  else:
    if debut+longueur<len(s):
      fin=debut+longueur
  for i in range(debut,debut+longueur): 
    res=fin
  return res